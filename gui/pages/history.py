"""
                Copyright (C) 2020 Theodoros Siklafidis

    This file is part of GRATIS.

    GRATIS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GRATIS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GRATIS. If not, see <https://www.gnu.org/licenses/>.
"""

import json
from tkinter import ttk, Canvas, PhotoImage, TclError

from conf.base import MAIN_FRAME_BACKGROUND, DELETE_IMAGE_PATH, DOWN_IMAGE_PATH, UP_IMAGE_PATH, \
    HISTORY_PAGE_DELETE_BUTTON_FALLBACK_TEXT, HISTORY_PAGE_MORE_BUTTON_FALLBACK_TEXT, \
    HISTORY_PAGE_LESS_BUTTON_FALLBACK_TEXT, HISTORY_PAGE_BACK_BUTTON_TEXT, MAIN_WINDOW_DIMENSIONS_STR
from gui.pages.mousewheel import MousewheelSupport
from gui.pages.page import Page
from os_recon.define_os import platform_type
from sqlite3_db.database import Graph


class GraphHistoryPage(Page):
    def __init__(self, parent, controller):
        super(GraphHistoryPage, self).__init__(parent)

        self.parent = parent
        self.controller = controller

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.graph_connection_handler = Graph()

        self.graphs = []
        self.graph_mini_frames = []
        self.graph_label_id = []
        self.buttons_frames = []
        self.delete_buttons = []
        self.more_buttons = []
        self.less_buttons = []
        self.load_counter = 0
        self._job = None
        self.chunk_size = 5
        self.chunks = list(range(0, self.graph_connection_handler.count() + self.chunk_size, self.chunk_size))
        self.chunk_index = 0

        self.canvas = Canvas(self, borderwidth=0, background=MAIN_FRAME_BACKGROUND, highlightthickness=1,
                             highlightbackground=MAIN_FRAME_BACKGROUND)
        self.graphs_frame = ttk.Frame(self.canvas)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="news")
        self.canvas.create_window((4, 4), window=self.graphs_frame, anchor="nw",
                                  tags="self.graphs_frame")
        self.graphs_frame.bind("<Configure>", self.on_frame_configure)
        MousewheelSupport(self).add_support_to(self.canvas, yscrollbar=self.vsb, what="units")

        self.back_button = ttk.Button(self, text=HISTORY_PAGE_BACK_BUTTON_TEXT,
                                      command=lambda: self.back(self.controller))
        self.back_button.grid(row=1, column=0, ipady=10, ipadx=15, pady=10, sticky="e")

    def on_raise(self):
        self.chunks = list(range(0, self.graph_connection_handler.count() + self.chunk_size, self.chunk_size))
        self.scroll_position_check()

    def fetch_chunk(self):
        if self.chunk_index < len(self.chunks):
            chunk = self.graph_connection_handler.chunk(self.chunks[self.chunk_index], self.chunk_size, _reversed=True)
            self.chunk_index += 1
            return chunk
        return None

    def create_graph_row_widgets(self, graphs):
        for graph in graphs:
            graph_contents = ''

            self.graph_mini_frames.append(
                ttk.Frame(self.graphs_frame, height=77, borderwidth="1", relief="solid"))
            if platform_type == "Windows":
                self.graph_mini_frames[-1].config(width=900)
            else:
                self.graph_mini_frames[-1].config(width=1000)
            self.graph_mini_frames[-1].grid_propagate(False)
            self.graph_mini_frames[-1].rowconfigure(0, weight=1)
            self.graph_mini_frames[-1].columnconfigure(1, weight=1)

            self.graph_label_id.append(
                ttk.Label(self.graph_mini_frames[-1], text=f"{self.load_counter + 1}", font='Arial 18 bold',
                          style='HistoryPage.Counter.TLabel'))
            self.graph_label_id[-1].grid_propagate(0)

            graph_contents += f"Generated at: {graph[2]}\n"

            for k, v in json.loads(graph[1]).items():
                graph_contents += f"{k.replace('_', ' ')}: {v}\n"

            self.graphs.append(
                ttk.Label(self.graph_mini_frames[-1], text=graph_contents, style='HistoryPage.Content.TLabel',
                          font='Arial 15'))

            self.buttons_frames.append(ttk.Frame(self.graph_mini_frames[-1], width=300))
            self.buttons_frames[-1].grid_propagate(False)
            self.buttons_frames[-1].rowconfigure(0, weight=1)
            self.buttons_frames[-1].columnconfigure(0, weight=1)
            self.buttons_frames[-1].columnconfigure(1, weight=1)

            try:
                delete_graph = PhotoImage(file=DELETE_IMAGE_PATH)
                self.delete_buttons.append(ttk.Button(self.buttons_frames[-1], image=delete_graph,
                                                      command=lambda x=(int(self.load_counter), graph[0]):
                                                      self.delete_button_func(x[0], x[1])))
                self.delete_buttons[-1].image = delete_graph

                more_graph = PhotoImage(file=DOWN_IMAGE_PATH)
                self.more_buttons.append(
                    ttk.Button(self.buttons_frames[-1], image=more_graph, text=self.load_counter,
                               command=lambda x=int(self.load_counter): self.more_button_func(x)))
                self.more_buttons[-1].image = more_graph

                less_graph = PhotoImage(file=UP_IMAGE_PATH)
                self.less_buttons.append(
                    ttk.Button(self.buttons_frames[-1], image=less_graph, text=self.load_counter,
                               command=lambda x=int(self.load_counter): self.less_button_func(x)))
                self.less_buttons[-1].image = less_graph
            except TclError:
                self.delete_buttons.append(ttk.Button(self.buttons_frames[-1],
                                                      text=HISTORY_PAGE_DELETE_BUTTON_FALLBACK_TEXT,
                                                      command=lambda x=(int(self.load_counter), graph[0]):
                                                      self.delete_button_func(x[0], x[1])))
                self.more_buttons.append(ttk.Button(self.buttons_frames[-1],
                                                    text=HISTORY_PAGE_MORE_BUTTON_FALLBACK_TEXT,
                                                    command=lambda x=int(self.load_counter): self.more_button_func(x)))
                self.less_buttons.append(ttk.Button(self.buttons_frames[-1],
                                                    text=HISTORY_PAGE_LESS_BUTTON_FALLBACK_TEXT,
                                                    command=lambda x=int(self.load_counter): self.less_button_func(x)))

            self.graph_mini_frames[self.load_counter].grid(pady=10, padx=10, sticky="news")
            self.graph_label_id[self.load_counter].grid(row=0, column=0, sticky="news", padx=10)
            self.graphs[self.load_counter].grid(row=0, column=1, sticky='nesw')
            self.buttons_frames[self.load_counter].grid(row=0, column=2, sticky="news")
            self.delete_buttons[self.load_counter].grid(row=0, column=0, sticky="n")
            self.more_buttons[self.load_counter].grid(row=0, column=1, sticky="ne", padx=(0, 20))
            self.update()
            self.update_idletasks()
            self.load_counter += 1

    def fetch_fresh_data(self):
        chunk = self.fetch_chunk()
        if chunk:
            self.create_graph_row_widgets(chunk)

    def scroll_position_check(self):
        try:
            if self.vsb.get()[1] == 1.0 or len(self.graph_mini_frames) == 0:
                self.fetch_fresh_data()
        except IndexError:
            if self.scroll_position_check is not None:
                self.after_cancel(self._job)
        self._job = self.after(200, self.scroll_position_check)

    def more_button_func(self, button_id):
        self.graph_mini_frames[button_id].configure(height=270)
        self.less_buttons[button_id].grid(row=0, column=1, sticky="ne", padx=(0, 20))

    def less_button_func(self, button_id):
        self.graph_mini_frames[button_id].configure(height=77)
        self.less_buttons[button_id].grid_forget()

    def delete_button_func(self, button_id, graph_id):
        if self.graph_connection_handler.delete(graph_id):
            self.graph_mini_frames[button_id].grid_forget()

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def back(self, controller):
        self.after_cancel(self._job)
        self.clean_old_data()
        controller.show_frame(self.retrieve_frame(controller, 'MainPage'), MAIN_WINDOW_DIMENSIONS_STR)

    def clean_old_data(self):
        for frame in self.graph_mini_frames:
            frame.grid_forget()
        self.graphs.clear()
        self.graph_mini_frames.clear()
        self.graph_label_id.clear()
        self.buttons_frames.clear()
        self.delete_buttons.clear()
        self.more_buttons.clear()
        self.less_buttons.clear()
        self.load_counter = 0
        self.canvas.yview_moveto(0)
        self.chunk_index = 0

    def destroy(self):
        self.graph_connection_handler.close()
        super(GraphHistoryPage, self).destroy()

    def refresh_widget_style(self, style):
        super(GraphHistoryPage, self).refresh_widget_style(style=style)
        self.canvas.configure(background=style['main_frame_bg'], highlightbackground=style['main_frame_bg'])
