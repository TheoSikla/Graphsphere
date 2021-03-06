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
from conf.general import STYLES_PATH
from platform import system

from conf.settings import get_theme

with open(STYLES_PATH) as f:
    try:
        STYLES = json.load(f)
    except Exception:
        exit(1)


# Define dimensions
MAIN_WINDOW_DIMENSIONS = STYLES['dimensions']['main'][system().lower()]
MAIN_WINDOW_DIMENSIONS_STR = 'x'.join([str(MAIN_WINDOW_DIMENSIONS['width']), str(MAIN_WINDOW_DIMENSIONS['height'])])

SETTINGS_WINDOW_DIMENSIONS = STYLES['dimensions']['settings'][system().lower()]
SETTINGS_WINDOW_WIDTH = SETTINGS_WINDOW_DIMENSIONS['width']
SETTINGS_WINDOW_HEIGHT = SETTINGS_WINDOW_DIMENSIONS['height']
SETTINGS_WINDOW_DIMENSIONS_STR = 'x'.join([str(SETTINGS_WINDOW_DIMENSIONS['width']),
                                           str(SETTINGS_WINDOW_DIMENSIONS['height'])])

LOGIN_WINDOW_DIMENSIONS = STYLES['dimensions']['login'][system().lower()]
LOGIN_WINDOW_WIDTH = LOGIN_WINDOW_DIMENSIONS['width']
LOGIN_WINDOW_HEIGHT = LOGIN_WINDOW_DIMENSIONS['height']
LOGIN_WINDOW_DIMENSIONS_STR = 'x'.join([str(LOGIN_WINDOW_DIMENSIONS['width']), str(LOGIN_WINDOW_DIMENSIONS['height'])])

# Define Style
ACTIVE_STYLE = get_theme()
STYLE = STYLES['styles'][ACTIVE_STYLE]

# Menu
MENU_BACKGROUND = STYLE['menu']['bg']
MENU_FOREGROUND = STYLE['menu']['fg']
MENU_RELIEF = STYLE['menu']['relief']
MENU_FONT = (
    STYLE['menu']['font']['family'], STYLE['menu']['font']['size'], STYLE['menu']['font']['style']
)

# Menu Items
MENU_ITEMS_BACKGROUND = STYLE['menu']['items']['bg']
MENU_ITEMS_FOREGROUND = STYLE['menu']['items']['fg']
MENU_ITEMS_RELIEF = STYLE['menu']['items']['relief']
MENU_ITEMS_FONT = (
    STYLE['menu']['items']['font']['family'], STYLE['menu']['items']['font']['size'],
    STYLE['menu']['items']['font']['style']
)

# Main Frame
MAIN_FRAME_BACKGROUND = STYLE['main_frame_bg']
MAIN_FRAME_PADX = 20
MAIN_FRAME_PADY = 20

# Button
BUTTON_FONT = (
    STYLE['button']['font']['family'], STYLE['button']['font']['size'], STYLE['button']['font']['style']
)
BUTTON_BACKGROUND = STYLE['button']['bg']
BUTTON_IMAGE_BACKGROUND = STYLE['button']['image_bg']
BUTTON_FOREGROUND = STYLE['button']['fg']
BUTTON_RELIEF = STYLE['button']['relief']
BUTTON_WIDTH = STYLE['button']['width']
BUTTON_INTERNAL_PAD_Y = STYLE['button']['internal_pad_y']

# Frame
FRAME_BACKGROUND = STYLE['frame']['bg']

# Radiobutton
RADIOBUTTON_FONT = (
    STYLE['radiobutton']['font']['family'], STYLE['radiobutton']['font']['size'], STYLE['radiobutton']['font']['style']
)
RADIOBUTTON_BACKGROUND = STYLE['radiobutton']['bg']
RADIOBUTTON_ACTIVE_BACKGROUND = STYLE['radiobutton']['active_bg']
RADIOBUTTON_FOREGROUND = STYLE['radiobutton']['fg']
RADIOBUTTON_RELIEF = STYLE['radiobutton']['relief']

# Checkbutton
CHECKBUTTON_FONT = (
    STYLE['checkbutton']['font']['family'], STYLE['checkbutton']['font']['size'], STYLE['checkbutton']['font']['style']
)
CHECKBUTTON_BACKGROUND = STYLE['checkbutton']['bg']
CHECKBUTTON_ACTIVE_BACKGROUND = STYLE['checkbutton']['active_bg']
CHECKBUTTON_FOREGROUND = STYLE['checkbutton']['fg']
CHECKBUTTON_RELIEF = STYLE['checkbutton']['relief']

# Label
LABEL_FONT_LARGE = (
    STYLE['label']['font']['family'], STYLE['label']['font']['size']['large'], STYLE['label']['font']['style']
)
LABEL_FONT_MEDIUM = (
    STYLE['label']['font']['family'], STYLE['label']['font']['size']['medium'], STYLE['label']['font']['style']
)
LABEL_BACKGROUND = STYLE['label']['bg']
LABEL_FOREGROUND = STYLE['label']['fg']
LABEL_RELIEF = STYLE['label']['relief']

# Label link
LABEL_LINK_FONT = (
    STYLE['label_link']['font']['family'], STYLE['label_link']['font']['size'], STYLE['label_link']['font']['style']
)
LABEL_LINK_BACKGROUND = STYLE['label_link']['bg']
LABEL_LINK_FOREGROUND = STYLE['label_link']['fg']
LABEL_LINK_CURSOR = STYLE['label_link']['cursor']

# Scrollable frame
SCROLLABLE_FRAME_FONT = (
    STYLE['scrollable_frame']['font']['family'],
    STYLE['scrollable_frame']['font']['size'],
    STYLE['scrollable_frame']['font']['style']
)
SCROLLABLE_FRAME_BACKGROUND = STYLE['scrollable_frame']['bg']
SCROLLABLE_FRAME_SCROLLBAR_BACKGROUND = STYLE['scrollable_frame']['scrollbar_bg']
SCROLLABLE_FRAME_TEXT_FOREGROUND = STYLE['scrollable_frame']['inserted_text']['fg']

NOTEBOOK_BACKGROUND = STYLE['notebook']['bg']
NOTEBOOK_TAB_STYLE = STYLE['notebook']['tab']
NOTEBOOK_TAB_BACKGROUND = NOTEBOOK_TAB_STYLE['bg']
NOTEBOOK_TAB_BACKGROUND_SELECTED = NOTEBOOK_TAB_STYLE['bg_selected']
NOTEBOOK_TAB_FOREGROUND = NOTEBOOK_TAB_STYLE['fg']
NOTEBOOK_TAB_FONT = (
    NOTEBOOK_TAB_STYLE['font']['family'],
    NOTEBOOK_TAB_STYLE['font']['size'],
    NOTEBOOK_TAB_STYLE['font']['style']
)


def reload():
    return STYLES['styles'][get_theme()]
