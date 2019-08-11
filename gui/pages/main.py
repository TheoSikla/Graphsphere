from gui.pages.page import *


class MainPage(Page):

    def __init__(self, parent, controller):
        Page.__init__(self, parent)

        # MainPage Frame configuration
        self.configure(bg="azure3")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(7, weight=1)
        # ================================

        # Button configuration variables
        self.ipady = 10
        # ================================

        # Main Label
        self.main_label = Label(self, bg="azure3", text="Welcome to Graph Sphere\n",
                                font=("Arial", 20, "bold"))
        # self.main_label.grid(row=1, column=1, columnspan=3)
        # ================================

        # Generate area button
        self.generate_area = ttk.Button(self, text="Generate Graph",
                                        command=lambda: controller.show_frame(self.retrieve_frame(controller, 'GraphGeneratePage'), transform))
        self.generate_area.grid(row=2, column=1, ipady=self.ipady, padx=30)
        # ================================

        # Analyze area button
        self.analyze_area = ttk.Button(self, text="Analyze Graph",
                                       command=lambda: controller.show_frame(
                                           self.retrieve_frame(controller, 'GraphAnalyzePage'), transform)
                                       )
        self.analyze_area.grid(row=2, column=2, ipady=self.ipady, padx=30)
        # ================================

        # Visualize area button
        self.visualise_area = ttk.Button(self, text="Visualize Graph",
                                         command=lambda: controller.show_frame(
                                             self.retrieve_frame(controller, 'GraphVisualizePage'), transform)
                                         )
        self.visualise_area.grid(row=2, column=3, ipady=self.ipady, padx=30)
        # ================================

        # Graph History area button
        self.graph_history_area = ttk.Button(self, text="Graph History",
                                             command=lambda: [controller.show_frame(
                                                 self.retrieve_frame(controller, 'GraphHistoryPage'), transform
                                             ),
                                                 self.retrieve_frame(controller, 'GraphHistoryPage').fecth_fresh_data()]
                                             )
        self.graph_history_area.grid(row=2, column=4, ipady=self.ipady, padx=30)
        # ================================

        # Exit button
        self.exit = ttk.Button(self, text="Exit", command=lambda: sys.exit(0))
        self.exit.grid(row=3, column=4, ipady=self.ipady, pady=20)
        # ================================
