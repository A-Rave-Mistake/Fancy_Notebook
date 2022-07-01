from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter import font


# ---- Variables ----

# Editor
bg_color = "#242329"
bg_lc_color = "#2e2c36"
insert_color = "#5cb557"
select_bgcolor = "#1ee897"
select_fgcolor = "#5fbbc2"

# Font
font_color = "white"
lc_font_color = "white"
bold = False
italic = False

# Info
lines = 1
pos = ""
chars = 0
file = None
file_name = False

# Menu References
font_menu = None
editor_menu = None



# ---- Classes ----

# Font Settings Menu
class Font_Menu:
    def __init__(self):
        # Construct widgets
        self.font_menu = Toplevel()
        self.font_menu.attributes('-topmost', True)
        self.font_menu.title("Font Settings")
        self.font_menu.resizable(False, False)

        # Open menu in correct location
        self.window_width = 250
        self.window_height = 150
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))
        self.font_menu.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x, y))

        # Font size
        self.f_size_label = Label(self.font_menu,
                             text="Font Size ",
                             font=("Arial", 10),
                             pady=10,
                             padx=5)
        self.f_size_label.grid(row=0, column=0)

        self.f_size_spinbox = Spinbox(self.font_menu,
                                 font=("Arial", 10),
                                 width=8,
                                 from_=1,
                                 to=72,
                                 textvariable=font_size,
                                 command=self.change_font_size)
        self.f_size_spinbox.grid(row=0, column=1)

        # Font style
        self.f_style_label = Label(self.font_menu,
                                    text="Font Family",
                                    font=("Arial", 10),
                                    pady=10,
                                    padx=5)
        self.f_style_label.grid(row=1, column=0)

        self.f_style_box = OptionMenu(self.font_menu,
                                      font_family,
                                      *font.families(),
                                      command=self.change_font_style,)
        self.f_style_box.grid(row=1, column=1)

        # Font color
        self.f_color_label = Label(self.font_menu,
                              text="Font Color",
                              font=("Arial", 10),
                              pady=5,
                              padx=5)
        self.f_color_label.grid(row=2, column=0)

        self.f_color_button = Button(self.font_menu,
                                bg=font_color,
                                width=10,
                                height=1,
                                command=self.change_font_color)
        self.f_color_button.grid(row=2, column=1)

        # Line counter font color
        self.lc_color_label = Label(self.font_menu,
                                   text="Line Counter Font Color",
                                   font=("Arial", 10),
                                   pady=5,
                                   padx=5)
        self.lc_color_label.grid(row=3, column=0)

        self.lc_color_button = Button(self.font_menu,
                                     bg=lc_font_color,
                                     width=10,
                                     height=1,
                                     command=self.change_lc_font_color)
        self.lc_color_button.grid(row=3, column=1)


    def change_font_color(self):
        color = colorchooser.askcolor(title="Choose Font Color")[1]
        global font_color
        font_color = color
        text_area.config(fg=color)
        self.f_color_button.config(bg=color)

    def change_lc_font_color(self):
        color = colorchooser.askcolor(title="Choose Line Counter Font Color")[1]
        global lc_font_color
        lc_font_color = color
        text_line.config(fg=color)
        self.lc_color_button.config(bg=color)

    def change_font_size(self):
        text_area.config(font=(font_family.get(), font_size.get()))

    def change_font_style(self, *args):
        text_area.config(font=(font_family.get(), font_size.get()))


# Editor Settings Menu
class Editor_Menu():
    def __init__(self):
        # Construct widgets
        self.editor_menu = Toplevel()
        self.editor_menu.attributes('-topmost', True)
        self.editor_menu.title("Editor Settings")
        self.editor_menu.resizable(False, False)

        # Open menu in correct location
        self.window_width = 250
        self.window_height = 175
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))
        self.editor_menu.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x, y))

        # Editor bg color
        self.e_color_label = Label(self.editor_menu,
                                   text="Editor Color",
                                   font=("Arial", 10),
                                   pady=5,
                                   padx=5)
        self.e_color_label.grid(row=0, column=0)

        self.e_color_button = Button(self.editor_menu,
                                     bg=bg_color,
                                     width=10,
                                     height=1,
                                     command=self.change_editor_color)
        self.e_color_button.grid(row=0, column=1)

        # Line counter bg color
        self.lc_color_label = Label(self.editor_menu,
                                   text="Line Counter Color",
                                   font=("Arial", 10),
                                   pady=5,
                                   padx=5)
        self.lc_color_label.grid(row=1, column=0)

        self.lc_color_button = Button(self.editor_menu,
                                     bg=bg_lc_color,
                                     width=10,
                                     height=1,
                                     command=self.change_linecount_color)
        self.lc_color_button.grid(row=1, column=1)

        # Line insert color
        self.insert_color_label = Label(self.editor_menu,
                                    text="Insert Cursor Color",
                                    font=("Arial", 10),
                                    pady=5,
                                    padx=5)
        self.insert_color_label.grid(row=2, column=0)

        self.insert_color_button = Button(self.editor_menu,
                                      bg=insert_color,
                                      width=10,
                                      height=1,
                                      command=self.change_insert_color)
        self.insert_color_button.grid(row=2, column=1)

        # Margin X size
        self.mx_size_label = Label(self.editor_menu,
                                  text="Margin Horizontal",
                                  font=("Arial", 10),
                                  pady=10,
                                  padx=5)
        self.mx_size_label.grid(row=3, column=0)

        self.mx_size_spinbox = Spinbox(self.editor_menu,
                                      font=("Arial", 10),
                                      width=8,
                                      from_=1,
                                      to=72,
                                      textvariable=margin_x,
                                      command=self.change_margin_size)
        self.mx_size_spinbox.grid(row=3, column=1)

        # Margin Y size
        self.my_size_label = Label(self.editor_menu,
                                   text="Margin Vertical",
                                   font=("Arial", 10),
                                   pady=10,
                                   padx=5)
        self.my_size_label.grid(row=4, column=0)

        self.my_size_spinbox = Spinbox(self.editor_menu,
                                       font=("Arial", 10),
                                       width=8,
                                       from_=1,
                                       to=72,
                                       textvariable=margin_y,
                                       command=self.change_margin_size)
        self.my_size_spinbox.grid(row=4, column=1)


    def change_editor_color(self):
        color = colorchooser.askcolor(title="Choose Editor Color")[1]
        global bg_color
        bg_color = color
        text_area.config(bg=color)
        self.e_color_button.config(bg=color)

    def change_linecount_color(self):
        color = colorchooser.askcolor(title="Choose Line Counter Color")[1]
        global bg_lc_color
        bg_lc_color = color
        text_line.config(bg=color)
        self.lc_color_button.config(bg=color)

    def change_insert_color(self):
        color = colorchooser.askcolor(title="Choose Insert Cursor Color")[1]
        global insert_color
        insert_color = color
        text_area.config(insertbackground=insert_color)

    def change_margin_size(self):
        global margin_y
        global margin_x
        margin_x = self.mx_size_spinbox.get()
        margin_y = self.my_size_spinbox.get()
        text_area.config(pady=margin_y, padx=margin_x)
        text_line.config(pady=margin_y)



# ---- Functions ----

# Files
def new_file():
    clear_text()
    root.title("New Text File")

# Open target text file
def open_file():
    file = filedialog.askopenfilename(initialdir="C:/",
                                      title="Open File",
                                      filetypes=(("Text Files", "*.txt"),
                                                 ("HTML Files", "*.html"),
                                                 ("CSS Files", "*.css"),
                                                 ("All Files", "*.*")))

    if file:
        global file_name
        file_name = file
        clear_text()
        root.title(file)
        file = open(file, "r")
        file_contents = file.read()
        text_area.insert(END, file_contents)
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
        global file
        file = file1
        root.title(file)
        file = open(file, "w")
        file.write(text_area.get(1.0, END))
        file.close()

def save_file():
    global file_name
    if file_name:
        file = open(file_name, "w")
        file.write(text_area.get(1.0, END))
        file.close()


# Font Customization
def open_font_menu():
    global font_menu
    font_menu = Font_Menu()

def open_editor_menu():
    global editor_menu
    editor_menu = Editor_Menu()

def set_font_bold():
    global bold
    if bold is False:
        bold = True
        text_area.config(font=(font_family.get(), font_size.get(), "bold"))
    else:
        bold = False
        text_area.config(font=(font_family.get(), font_size.get()))

def set_font_italic():
    global italic
    if italic is False:
        italic = True
        text_area.config(font=(font_family.get(), font_size.get(), "italic"))
    else:
        italic = False
        text_area.config(font=(font_family.get(), font_size.get()))


# Editor Customization
def change_selection_bgcolor():
    color = colorchooser.askcolor(title="Choose Selection Color")[1]
    global select_bgcolor
    select_bgcolor = color
    text_area.config(selectbackground=color)


def change_selection_fgcolor():
    color = colorchooser.askcolor(title="Choose Selection Color")
    global select_fgcolor
    select_fgcolor = color
    text_area.config(selectforeground=color)


# Actions
def rc_popup(e):
    rc_menu.tk_popup(e.x_root, e.y_root)

def clear_text():
    text_area.delete(1.0, END)
    global lines
    lines = 1
    update_lines()

def select_all():
    text_area.tag_add('sel', 1.0, END)

def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def undo():
    text_area.event_generate("<<Undo>>")

def quit():
    root.destroy()


# TODO: Bookmarks
#def go_to_line():
    #text_area.mark_set("insert", "%d.%d" % (2, 5))


# Dirty Secrets
def update_lines():
    global lines
    lines = int(text_area.index('end-1c').split('.')[0])
    global chars
    chars = int(max(0, (len(text_area.get(1.0, END)))-1))
    global pos
    pos = str(text_area.index('insert'))
    info_bar.config(text="Lines: {}  Chars: {} | Position: {}".format(lines, chars, pos))

    get_new_line(lines)

def new_line_1():
    text_line.config(state=NORMAL)
    text_line.insert(1.0, "1")
    text_line.config(state=DISABLED)

def get_new_line(lines):
    text_line.config(state = NORMAL)
    # this detects new line in our notepad and adds line count to the left side
    if text_area.get(float("{}.0".format(lines)), END) == "\n":
        # if next line is empty and we backspace, the line count on the left gets deleted
        if len(text_area.get(float("{}.0".format(lines))+1, END)) == 0:
            text_line.delete(float("{}.0".format(lines)) + 1, END)
        # if we create a new line and there's no line number attached it creates one
        if text_line.get(float("{}.0".format(lines)), END) == "":
            text_line.insert(float("{}.0".format(lines)), "\n")
            text_line.insert(float("{}.0".format(lines)), lines)

    text_line.config(state=DISABLED)

def key_handler(event=None):
    if event and event.keysym:
        update_lines()



# ---- GUI ----

# Main Window
root = Tk()
root.title("Fancy Notepad")

# Window Size
window_width = 800
window_height = 550

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Editor Settings
margin_x = StringVar(root)
margin_x.set("10")
margin_y = StringVar(root)
margin_y.set("10")

# Font Settings
font_size = StringVar(root)
font_size.set(20)
font_family = StringVar(root)
font_family.set("Arial")

# Main Frame
mainFrame = Frame(root, width=1920, height=965)
#mainFrame.pack(pady=5, expand=True, fill="both")
mainFrame.grid()
mainFrame.grid_propagate(False)
mainFrame.grid_rowconfigure(1, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)

# Scroll Bar
scroll_bar = Scrollbar(mainFrame)
#scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.grid(row=0, column=2, sticky=E + S + N)

text_line = Text(mainFrame,
                 width=3,
                 height=30,
                 font=(font_family, font_size.get()),
                 yscrollcommand=scroll_bar.set,
                 bg=bg_lc_color,
                 fg=lc_font_color,
                 insertbackground=insert_color,
                 state=DISABLED,
                 padx=2,
                 pady=int(margin_y.get()))
#text_area.pack(expand=True, fill=Y)
text_line.grid(row=0, column=0, sticky=N + E + S + W)

# Main Text Area
text_area = Text(mainFrame,
                 width=122,
                 height=25,
                 font=(font_family.get(), font_size.get()),
                 selectbackground=select_bgcolor,
                 selectforeground=select_fgcolor,
                 undo=True,
                 yscrollcommand=scroll_bar.set,
                 padx=int(margin_x.get()),
                 pady=int(margin_y.get()),
                 bg=bg_color,
                 fg=font_color,
                 insertbackground=insert_color)
#text_area.pack(expand=True, fill="both")
text_area.grid(row=0, column=1, sticky=N + E + S + W)

scroll_bar.config(command=text_area.yview)

# Bottom Bar
bottom_bar = Label(root)
#bottom_bar.pack(side=BOTTOM)
bottom_bar.grid(row=1, column=0)

info_bar = Label(bottom_bar,
                 anchor=E,
                 padx=100,
                 text="Lines: 1  Chars: 0 | Position: 0.0",
                 font=("Arial", 10))
#info_bar.pack(side=LEFT)
info_bar.grid(row=0, column=0)

bold_button = Button(bottom_bar,
                     anchor=E,
                     text="B",
                     font=("Arial", 10, "bold"),
                     padx=5,
                     command=set_font_bold,
                     bg="lightgray")
#bold_button.pack(side=RIGHT)
bold_button.grid(row=0, column=1)

italic_button = Button(bottom_bar,
                     anchor=E,
                     text="I",
                     font=("Arial", 10, "italic"),
                     padx=5,
                     command=set_font_italic,
                     bg="lightgray")
#italic_button.pack(side=RIGHT)
italic_button.grid(row=0, column=2)

# Menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)

# Menu Bar - File Menu
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new_file)
#fileMenu.add_command(label="New Window")
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save As", command=save_as)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

# Menu Bar - Edit Menu
editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=undo)
editMenu.add_separator()
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Paste", command=paste)
editMenu.add_separator()
editMenu.add_command(label="Select All", command=select_all)
editMenu.add_separator()
editMenu.add_command(label="Clear", command=clear_text)

# Menu Bar - Preferences Bar
prefMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Preferences", menu=prefMenu)
prefMenu.add_command(label="Font Settings", command=open_font_menu)
prefMenu.add_command(label="Editor Settings", command=open_editor_menu)


# Right Click Menu Bar
rc_menu = Menu(root, tearoff=False)
rc_menu.add_command(label="Copy", command=copy)
rc_menu.add_command(label="Paste", command=paste)
rc_menu.add_command(label="Cut", command=cut)
rc_menu.add_separator()
rc_menu.add_command(label="Select All", command=select_all)
rc_menu.add_separator()
rc_menu.add_command(label="Clear", command=clear_text)
root.bind("<Button-3>", rc_popup)



# ---- Initialize ----
root.bind('<Key>', key_handler)
new_line_1()
root.mainloop()
