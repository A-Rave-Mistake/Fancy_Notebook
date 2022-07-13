from tkinter import *
from tkinter import ttk
from tkinter import filedialog, colorchooser
from tkinter import font

import menus
import functions


# Menu References
main_window = None
root_window = None
font_menu = None
editor_menu = None
num_menu = None

# Note Tabs
tab_master = None
current_tab = 0

# Text area and line counter
text_area_selected = None
text_line = None

# Contains text of the currently selected Note Tab
text = ""
saved_text = ""



# Detect key presses so the script gains info on character & line count and insert marker position
def key_handler(event=None):
    if event and event.keysym:
        functions.update_lines()
        functions.savetext()
        functions.check_for_changes()



# Initialize the notepad
if __name__ == "__main__":
    functions.initialize()