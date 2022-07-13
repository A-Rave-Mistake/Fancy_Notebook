from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, filedialog, font
from datetime import datetime
from os import path
from random import randint

import main
import menus

# Main
def initialize():
    main.main_window = menus.Window()
    main.root_window = main.main_window.rootw
    main.text_area_selected = main.main_window.text_area
    main.text_line = main.main_window.text_line
    main.tab_master.container.config(bg=main.main_window.bg_color)
    main.root_window.bind('<Key>', main.key_handler)
    new_line_init()
    main.root_window.mainloop()

# Files
def new_file():
    clear_text()
    main.root_window.title("New Text File")

# Open target text file
def open_file():
    file = filedialog.askopenfilename(initialdir="C:/",
                                      title="Open File",
                                      filetypes=(("Text Files", "*.txt"),
                                                 ("HTML Files", "*.html"),
                                                 ("CSS Files", "*.css"),
                                                 ("All Files", "*.*")))

    if file:
        main.main_window.file_name = file
        clear_text()
        file = open(file, "r")
        file_contents = file.read()

        clear_text()
        new_tab = main.tab_master.add_tab()
        new_tab.text = file_contents
        main.text = file_contents
        main.saved_text = file_contents
        name = path.basename(file.name)
        main.tab_master.tabs[main.current_tab].tab_name = name
        main.tab_master.tabs[main.current_tab].button1.config(text=name)
        main.text_area_selected.insert(1.0, file_contents)
        file.close()
        update_lines()

# Save document as
def save_as():
    file1 = filedialog.asksaveasfilename(initialdir="C:/",
                                        defaultextension="*.*",
                                        title="Save File",
                                        filetypes=(("Text Files", "*.txt"),
                                                 ("HTML Files", "*.html"),
                                                 ("CSS Files", "*.css"),
                                                 ("All Files", "*.*")))
    if file1:
        main.main_window.file = file1
        main.root_window.title(main.main_window.file)
        file = open(main.main_window.file, "w")
        file.write(main.text_area_selected.get(1.0, END))
        file.close()

def save_file():
    if main.main_window.file_name:
        file = open(main.main_window.file_name, "w")
        file.write(main.text_area_selected.get(1.0, END))
        file.close()


# Font Customization
def open_font_menu():
    main.font_menu = menus.Font_Menu()

def open_editor_menu():
    main.editor_menu = menus.Editor_Menu()

def open_random_number_menu():
    main.num_menu = menus.Number_Menu()

def set_font_bold():
    if main.main_window.bold is False:
        main.main_window.bold = True
        main.text_area_selected.config(font=(main.root_window.font_family.get(), main.root_window.font_size.get(), "bold"))
    else:
        main.main_window.bold = False
        main.text_area_selected.config(font=(main.root_window.font_family.get(), main.root_window.font_size.get()))

def set_font_italic():
    if main.main_window.italic is False:
        main.main_window.italic = True
        main.text_area_selected.config(font=(main.root_window.font_family.get(), main.root_window.font_size.get(), "italic"))
    else:
        main.main_window.italic = False
        main.text_area_selected.config(font=(main.root_window.font_family.get(), main.root_window.font_size.get()))

def selection_italic():
    pass

def selection_bold():
    pass



# Editor Customization
def change_selection_bgcolor():
    color = colorchooser.askcolor(title="Choose Selection Color")[1]
    main.main_window.select_bgcolor = color
    main.text_area_selected.config(selectbackground=color)


def change_selection_fgcolor():
    color = colorchooser.askcolor(title="Choose Selection Color")
    main.main_window.select_fgcolor = color
    main.text_area_selected.config(selectforeground=color)


# Actions
def rc_popup(e):
    main.main_window.rc_menu.tk_popup(e.x_root, e.y_root)

def clear_text():
    main.text_area_selected.delete(1.0, END)
    main.main_window.lines = 1
    update_lines()

def select_all():
    main.text_area_selected.tag_add('sel', 1.0, END)

def copy():
    main.text_area_selected.event_generate("<<Copy>>")

def cut():
    main.text_area_selected.event_generate("<<Cut>>")

def paste():
    main.text_area_selected.event_generate("<<Paste>>")

def undo():
    main.text_area_selected.event_generate("<<Undo>>")

def quit():
    main.root_window.destroy()

# Selected part of the text file becomes uppercase
def upper_selection():
    selection = [main.text_area_selected.index("sel.first"), main.text_area_selected.index("sel.last")]
    uppertext = main.text_area_selected.get(selection[0], selection[1]).upper()
    main.text_area_selected.delete(selection[0], selection[1])
    main.text_area_selected.insert(selection[0], uppertext)

# Same as above except lowercase
def lower_selection():
    selection = [main.text_area_selected.index("sel.first"), main.text_area_selected.index("sel.last")]
    lowertext = main.text_area_selected.get(selection[0], selection[1]).lower()
    main.text_area_selected.delete(selection[0], selection[1])
    main.text_area_selected.insert(selection[0], lowertext)

# Capitalize selected text
def capitalize_selection():
    selection = [main.text_area_selected.index("sel.first"), main.text_area_selected.index("sel.last")]
    splittext = main.text_area_selected.get(selection[0], selection[1]).split(" ")
    capitalizedtext = ' '.join([f.capitalize() for f in splittext])
    main.text_area_selected.delete(selection[0], selection[1])
    main.text_area_selected.insert(selection[0],  capitalizedtext)

# Makes the selected text reversed
def reverse_selection():
    selection = [main.text_area_selected.index("sel.first"), main.text_area_selected.index("sel.last")]
    reversetext = main.text_area_selected.get(selection[0], selection[1])[::-1]
    main.text_area_selected.delete(selection[0], selection[1])
    main.text_area_selected.insert(selection[0], reversetext)



# TODO: Bookmarks
#def go_to_line():
    #text_area.mark_set("insert", "%d.%d" % (2, 5))

def check_for_changes():
    if main.text != main.saved_text:
        main.tab_master.tabs[main.current_tab].button1.config(text=str.format('{}*', main.tab_master.tabs[main.current_tab].tab_name))

# Line Counter
def update_lines():
    main.main_window.lines = int(main.text_area_selected.index('end-1c').split('.')[0])
    main.main_window.chars = int(max(0, (len(main.text_area_selected.get(1.0, END).replace("\n", "")))))
    main.main_window.pos = str(main.text_area_selected.index('insert'))
    main.main_window.info_bar.config(text="Lines: {}  Chars: {} | Position: {}".format(main.main_window.lines, main.main_window.chars, main.main_window.pos))

    get_new_line(main.main_window.lines)

def new_line_init():
    main.text_line.config(state=NORMAL)
    main.text_line.insert(1.0, "1")
    main.text_line.config(state=DISABLED)

def get_new_line(lines):
    main.text_line.config(state = NORMAL)
    # this detects new line in our notepad and adds line count to the left side
    if main.text_area_selected.get(float("{}.0".format(lines)), END) == "\n":
        # if next line is empty and we backspace, the line count on the left gets deleted
        if len(main.text_area_selected.get(float("{}.0".format(lines))+1, END)) == 0:
            main.text_line.delete(float("{}.0".format(lines)) + 1, END)
        # if we create a new line and there's no line number attached it creates one
        if main.text_line.get(float("{}.0".format(lines)), END) == "":
            main.text_line.insert(float("{}.0".format(lines)), "\n")
            main.text_line.insert(float("{}.0".format(lines)), lines)
    elif len(main.text_area_selected.get(float("{}.0".format(lines))+1, END)) == 0:
            main.text_line.delete(float("{}.0".format(lines)) + 1, END)

    main.text_line.config(state=DISABLED)



# Tabs

# Save the text inside a tab
def savetext():
    main.text = main.text_area_selected.get(1.0, END)
    main.saved_text = main.text_area_selected.get(1.0, END)
    main.tab_master.tabs[main.current_tab].text = main.text



# Inserts
now = datetime.now()
date_formats = ["%A", "%X %p", "%x", "%A %c %p"]

def insert_weekday():
    main.text_area_selected.insert(main.text_area_selected.index('insert'), now.strftime(date_formats[0]))

def insert_time():
    main.text_area_selected.insert(main.text_area_selected.index('insert'), now.strftime(date_formats[1]))

def insert_date():
    main.text_area_selected.insert(main.text_area_selected.index('insert'), now.strftime(date_formats[2]))

def insert_date_full():
    main.text_area_selected.insert(main.text_area_selected.index('insert'), now.strftime(date_formats[3]))

def insert_random_number():
    main.text_area_selected.insert(main.text_area_selected.index('insert'), randint(int(main.main_window.random_num_min.get()), int(main.main_window.random_num_max.get())))