from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, filedialog, font

from functions import *
import main


# Root Window
class Window:
    def __init__(self):

        # Create Window Widget
        self.rootw = Tk()
        self.rootw.title("Fancy Notepad")
        self.icon = PhotoImage(file="notebook.png")
        # Icon downloaded from game-icons.net
        self.rootw.iconphoto(True, self.icon)

        # Window Size
        self.window_width = 800
        self.window_height = 550

        self.screen_width = self.rootw.winfo_screenwidth()
        self.screen_height = self.rootw.winfo_screenheight()

        x = int((self.screen_width / 2) - (self.window_width / 2))
        y = int((self.screen_height / 2) - (self.window_height / 2))

        self.rootw.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x, y))


        # Info
        self.lines = 1
        self.pos = ""
        self.chars = 0
        self.file = None
        self.file_name = False

        # Editor Settings
        self.margin_x = StringVar(self.rootw)
        self.margin_x.set("10")
        self.margin_y = StringVar(self.rootw)
        self.margin_y.set("10")

        self.bg_color = "#242329"
        self.bg_lc_color = "#2e2c36"
        self.insert_color = "#5cb557"
        self.select_bgcolor = "#1ee897"
        self.select_fgcolor = "#5fbbc2"

        # Random Number Generator Settings
        self.random_num_min = StringVar(self.rootw)
        self.random_num_min.set("0")
        self.random_num_max = StringVar(self.rootw)
        self.random_num_max.set("100")

        # Font Settings
        self.font_size = StringVar(self.rootw)
        self.font_size.set(20)
        self.font_family = StringVar(self.rootw)
        self.font_family.set("Arial")

        self.font_color = "white"
        self.lc_font_color = "#c7c7c7"
        self.bold = False
        self.italic = False

        # Tab Container
        tab_master = TabContainer(self.rootw)
        main.tab_master = tab_master

        # Main Frame
        self.mainFrame = Frame(self.rootw, width=1920, height=933)
        # mainFrame.pack(pady=5, expand=True, fill="both")
        self.mainFrame.grid(row=1)
        self.mainFrame.grid_propagate(False)
        self.mainFrame.grid_rowconfigure(1, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        # Scroll Bar
        self.scroll_bar = Scrollbar(self.mainFrame)
        # scroll_bar.pack(side=RIGHT, fill=Y)
        self.scroll_bar.grid(row=0, column=2, sticky=E + S + N)

        self.text_line = Text(self.mainFrame,
                                width=3,
                                height=30,
                                font=(self.font_family, self.font_size.get()),
                                yscrollcommand=self.scroll_bar.set,
                                bg=self.bg_lc_color,
                                fg=self.lc_font_color,
                                insertbackground=self.insert_color,
                                state=DISABLED,
                                padx=2,
                                pady=int(self.margin_y.get()))
        # text_area.pack(expand=True, fill=Y)
        self.text_line.grid(row=0, column=0, sticky=N + E + S + W)

        # Main Text Area
        self.text_area = Text(self.mainFrame,
                                width=122,
                                height=25,
                                font=(self.font_family.get(), self.font_size.get()),
                                selectbackground=self.select_bgcolor,
                                selectforeground=self.select_fgcolor,
                                undo=True,
                                yscrollcommand=self.scroll_bar.set,
                                padx=int(self.margin_x.get()),
                                pady=int(self.margin_y.get()),
                                bg=self.bg_color,
                                fg=self.font_color,
                                insertbackground=self.insert_color)
        # text_area.pack(expand=True, fill="both")
        self.text_area.grid(row=0, column=1, sticky=N + E + S + W)

        main.text_area_selected = self.text_area

        # KEYBINDS
        #self.text_area.bind("<Control-o>", open_file)
        #self.text_area.bind("<Control-s>", save_file)
        #self.text_area.bind("<Control-Shift-S>", save_as)

        self.scroll_bar.config(command=self.text_area.yview)

        # Bottom Bar
        self.bottom_bar = Label(self.rootw)
        # bottom_bar.pack(side=BOTTOM)
        self.bottom_bar.grid(row=2, column=0, sticky=S)

        self.info_bar = Label(self.bottom_bar,
                        anchor=E,
                        padx=100,
                        text="Lines: 1  Chars: 0 | Position: 0.0",
                        font=("Arial", 10))
        # info_bar.pack(side=LEFT)
        self.info_bar.grid(row=0, column=0)

        self.bold_button = Button(self.bottom_bar,
                            anchor=E,
                            text="B",
                            font=("Arial", 10, "bold"),
                            padx=5,
                            command=set_font_bold,
                            bg="lightgray")
        # bold_button.pack(side=RIGHT)
        self.bold_button.grid(row=0, column=1)

        self.italic_button = Button(self.bottom_bar,
                                    anchor=E,
                                    text="I",
                                    font=("Arial", 10, "italic"),
                                    padx=5,
                                    command=set_font_italic,
                                    bg="lightgray")
        # italic_button.pack(side=RIGHT)
        self.italic_button.grid(row=0, column=2)

        # Menu Bar
        self.menuBar = Menu(self.rootw)
        self.rootw.config(menu=self.menuBar)

        # Menu Bar - File Menu
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="New", command=new_file)
        self.fileMenu.add_command(label="New Tab", command=main.tab_master.add_tab)
        self.fileMenu.add_command(label="Open", command=open_file)
        self.fileMenu.add_command(label="Save", command=save_file)
        self.fileMenu.add_command(label="Save As", command=save_as)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=quit)

        # Menu Bar - Edit Menu
        self.editMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Undo", command=undo)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Copy", command=copy)
        self.editMenu.add_command(label="Cut", command=cut)
        self.editMenu.add_command(label="Paste", command=paste)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Select All", command=select_all)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Clear", command=clear_text)

        # Menu Bar - Preferences Bar
        self.prefMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Preferences", menu=self.prefMenu)
        self.prefMenu.add_command(label="Font Settings", command=open_font_menu)
        self.prefMenu.add_command(label="Editor Settings", command=open_editor_menu)

        # Menu Bar - Tools Bar
        self.toolsbar = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Tools", menu=self.toolsbar)

        self.toolsbar_insert = Menu(self.toolsbar, tearoff=0)
        self.toolsbar.add_cascade(label="Insert", menu=self.toolsbar_insert)
        self.toolsbar_insert.add_command(label="Weekday", command=insert_weekday)
        self.toolsbar_insert.add_command(label="Date", command=insert_date)
        self.toolsbar_insert.add_command(label="Time", command=insert_time)
        self.toolsbar_insert.add_command(label="Full Date", command=insert_date_full)
        self.toolsbar_insert.add_separator()
        self.toolsbar_insert.add_command(label="Random Number", command=insert_random_number)
        self.toolsbar_insert.add_command(label="Random Number Settings", command=open_random_number_menu)

        # Right Click Menu Bar
        self.rc_menu = Menu(self.rootw, tearoff=False)
        self.rc_menu.add_command(label="Copy", command=copy)
        self.rc_menu.add_command(label="Paste", command=paste)
        self.rc_menu.add_command(label="Cut", command=cut)
        self.rc_menu.add_separator()
        self.rc_menu.add_command(label="Select All", command=select_all)
        self.rc_menu.add_separator()
        self.rc_menu.add_command(label="Clear", command=clear_text)
        self.rc_menu.add_separator()

        self.insertmenu = Menu(self.rc_menu, tearoff=False)
        self.rc_menu.add_cascade(label="Insert", menu=self.insertmenu)
        self.insertmenu.add_command(label="Weekday", command=insert_weekday)
        self.insertmenu.add_command(label="Time", command=insert_time)
        self.insertmenu.add_command(label="Date", command=insert_date)
        self.insertmenu.add_command(label="Full Date", command=insert_date_full)
        self.insertmenu.add_separator()
        self.insertmenu.add_command(label="Random Number", command=insert_random_number)
        self.rc_menu.add_separator()

        self.rc_menu.add_command(label="Uppercase", command=upper_selection)
        self.rc_menu.add_command(label="Lowercase", command=lower_selection)
        self.rc_menu.add_command(label="Capitalize", command=capitalize_selection)
        self.rc_menu.add_command(label="Reverse", command=reverse_selection)

        self.rootw.bind("<Button-3>", rc_popup)




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
        self.screen_width = main.root_window.winfo_screenwidth()
        self.screen_height = main.root_window.winfo_screenheight()
        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))
        self.font_menu.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x, self.y))

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
                                 textvariable=main.main_window.font_size,
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
                                      main.main_window.font_family,
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
                                bg=main.main_window.font_color,
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
                                     bg=main.main_window.lc_font_color,
                                     width=10,
                                     height=1,
                                     command=self.change_lc_font_color)
        self.lc_color_button.grid(row=3, column=1)


    def change_font_color(self):
        color = colorchooser.askcolor(title="Choose Font Color")[1]
        main.main_window.font_color = color
        main.main_window.text_area.config(fg=color)
        self.f_color_button.config(bg=color)

    # Change font color of the line counter
    def change_lc_font_color(self):
        color = colorchooser.askcolor(title="Choose Line Counter Font Color")[1]
        main.main_window.lc_font_color = color
        main.text_line.config(fg=color)
        self.lc_color_button.config(bg=color)

    def change_font_size(self):
        main.text_area_selected.config(font=(main.main_window.font_family.get(), main.main_window.font_size.get()))

    # Change font family
    def change_font_style(self, *args):
        main.text_area_selected.config(font=(main.main_window.font_family.get(), main.main_window.font_size.get()))
        main.text_line.config(font=(main.main_window.font_family.get(), main.main_window.font_size.get()))


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
        self.screen_width = main.root_window.winfo_screenwidth()
        self.screen_height = main.root_window.winfo_screenheight()
        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))
        self.editor_menu.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x, self.y))

        # Editor bg color
        self.e_color_label = Label(self.editor_menu,
                                   text="Editor Color",
                                   font=("Arial", 10),
                                   pady=5,
                                   padx=5)
        self.e_color_label.grid(row=0, column=0)

        self.e_color_button = Button(self.editor_menu,
                                     bg=main.main_window.bg_color,
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
                                     bg=main.main_window.bg_lc_color,
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
                                      bg=main.main_window.insert_color,
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
                                      textvariable=main.main_window.margin_x,
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
                                       textvariable=main.main_window.margin_y,
                                       command=self.change_margin_size)
        self.my_size_spinbox.grid(row=4, column=1)


    # Change editor background color
    def change_editor_color(self):
        color = colorchooser.askcolor(title="Choose Editor Color")[1]
        main.main_window.bg_color = color
        main.text_area_selected.config(bg=color)
        self.e_color_button.config(bg=color)

    # Change linecounter background color
    def change_linecount_color(self):
        color = colorchooser.askcolor(title="Choose Line Counter Color")[1]
        main.main_window.bg_lc_color = color
        main.text_line.config(bg=color)
        self.lc_color_button.config(bg=color)

    # Change insert line color
    def change_insert_color(self):
        color = colorchooser.askcolor(title="Choose Insert Cursor Color")[1]
        main.main_window.insert_color = color
        main.text_area_selected.config(insertbackground=color)
        self.insert_color_button.config(bg=color)

    # Change text margin
    def change_margin_size(self):
        main.main_window.margin_x = self.mx_size_spinbox.get()
        main.main_window.margin_y = self.my_size_spinbox.get()
        main.text_area_selected.config(pady=main.main_window.margin_y, padx=main.main_window.margin_x)
        main.text_line.config(pady=main.main_window.margin_y)



class Number_Menu:
    def __init__(self):
        # Construct widgets
        self.num_menu = Toplevel()
        self.num_menu.attributes('-topmost', True)
        self.num_menu.title("Random Number Settings")
        self.num_menu.resizable(False, False)

        # Open menu in correct location
        self.window_width = 175
        self.window_height = 80
        self.screen_width = main.root_window.winfo_screenwidth()
        self.screen_height = main.root_window.winfo_screenheight()
        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))
        self.num_menu.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x, self.y))

        self.num_min_label = Label(self.num_menu,
                                  text="Random Min ",
                                  font=("Arial", 10),
                                  pady=10,
                                  padx=5)
        self.num_min_label.grid(row=0, column=0)

        self.num_min_spinbox = Spinbox(self.num_menu,
                                      font=("Arial", 10),
                                      width=8,
                                      textvariable=main.main_window.random_num_min,
                                      )
        self.num_min_spinbox.grid(row=0, column=1)

        self.num_max_label = Label(self.num_menu,
                                   text="Random Max ",
                                   font=("Arial", 10),
                                   pady=10,
                                   padx=5)
        self.num_max_label.grid(row=1, column=0)

        self.num_max_spinbox = Spinbox(self.num_menu,
                                       font=("Arial", 10),
                                       width=8,
                                       textvariable=main.main_window.random_num_max,
                                       )
        self.num_max_spinbox.grid(row=1, column=1)



# Tabs

# Contains all note tabs
class TabContainer:
    def __init__(self, parent):
        self.tabs = []

        self.container = Frame(parent, width=1920, bg="black")
        self.container.grid(row=0, sticky=NSEW)
        self.tabholder = Frame(self.container)
        self.tabholder.pack(side=LEFT)
        self.addbutton = Button(self.container, text="+", font=("Arial", 8, "bold"), command=self.add_tab)
        self.addbutton.pack(padx=10, side=LEFT)

        self.add_tab1()

    def add_tab1(self):
        self.new_tab = Note_Tab(self.tabholder, len(self.tabs), True if len(self.tabs) == 0 else False)
        self.tabs.append(self.new_tab)
        self.new_tab.container.config(bg="#007aa5")
        self.new_tab.button1.config(text="Main")
        self.new_tab.tab_name = "Main"


    def add_tab(self):
        self.new_tab = Note_Tab(self.tabholder, len(self.tabs), True if len(self.tabs) == 0 else False)
        self.tabs.append(self.new_tab)
        self.new_tab.focus()
        return self.new_tab




# Single note tab
class Note_Tab:
    def __init__(self, parent, index, is_main):
        self.index = index
        self.is_main = is_main
        self.text = ""
        self.tab_name = f'New Tab #{self.index}'

        self.mainframe = Frame(parent, bg="#abaeb3")
        self.mainframe.pack(side=LEFT)
        self.container = Frame(self.mainframe, relief=RAISED, borderwidth=2, bg="#868b92")
        self.container.pack()
        self.button1 = Button(self.container, text=self.tab_name, width=15, font=("Arial", 8, "bold"), bg="#abaeb3", borderwidth=0, command=self.focus)
        self.button1.pack(side=LEFT, padx=2, pady=2)

        # Tab delete button, the 'main' tab doesn't have one
        if not self.is_main:
            self.button = Button(self.container, text="X", width=1, font=("Arial", 8, "bold"), bg="#b4b5b8", fg="red", borderwidth=0, command=self.remove)
            self.button.pack(padx=5, pady=2)


    def remove(self):
        main.tab_master.tabs[main.tab_master.tabs.index(self)-1].focus()
        main.tab_master.tabs.pop(main.tab_master.tabs.index(self))
        self.mainframe.destroy()

    def focus(self):
        if main.tab_master.tabs.index(self) != main.current_tab:
            self.container.config(bg="#007aa5")
            main.tab_master.tabs[main.current_tab].focus_lose()
            main.current_tab = main.tab_master.tabs.index(self)

            clear_text()
            main.text = ""
            main.text_area_selected.insert(1.0, self.text)

    def focus_lose(self):
        savetext()
        self.container.config(bg="#868b92")

    def save_text(self, input):
        self.text = input