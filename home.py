import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
from Journal import *

subtitle_tile = None

def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()


class app_tile:

    def __init__(self, frame, affecting_frame, row, column, width, text, font, function, background_colour, text_colour,
                 highlight_background, highlight_thickness, column_span):

        self.frame = frame
        self.row = row
        self.affecting_frame = affecting_frame
        self.column = column
        self.width = width
        self.text = text
        self.font = font
        self.function = function
        self.background = background_colour
        self.text_colour = text_colour
        self.highlight_background = highlight_background
        self.highlight_thickness = highlight_thickness
        self.column_span = column_span

    def create_tile(self):
        tile = tk.Button(self.frame, text=self.text, bg=self.background, fg=self.text_colour, font=self.font,
                         highlightbackground=self.highlight_background, highlightthickness=self.highlight_thickness,
                         command=self.function, width=self.width)
        tile.grid(row=self.row, column=self.column)

    def subtitle(app_tile_instance):
        global subtitle_tile
        if subtitle_tile is None:
            clear_frame(app_tile_instance.affecting_frame)
            subtitle_tile = tk.Label(window, text=app_tile_instance.text, bg='dark slate grey', fg='navajo white',
                        font=("Lucida Sans Typewriter", 20))
            subtitle_tile.grid(row=0, column=2, sticky="w")
            if app_tile_instance.text == 'Journal':
                launch_journal(info_frame)
            else:
                None

        else:
            clear_frame(app_tile_instance.affecting_frame)
            subtitle_tile.config(text=app_tile_instance.text)
            if app_tile_instance.text == 'Journal':
                launch_journal(info_frame)
            else:
                None


def home_setup(frame):
    journal_tile = app_tile(frame, info_frame, 0, 0, 10, "Journal", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: app_tile.subtitle(journal_tile), 'dark slate grey', 'navajo white', 
                            'navajo white', 1, column_span=1)
    journal_tile.create_tile()
    network_tile = app_tile(frame, info_frame, 1, 0, 10, "Network", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: app_tile.subtitle(network_tile), 'dark slate grey', 'navajo white', 
                            'navajo white', 1, column_span=1)
    network_tile.create_tile()
    health_tile = app_tile(frame, info_frame, 2, 0, 10, "Health", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: app_tile.subtitle(health_tile), 'dark slate grey', 'navajo white', 
                            'navajo white', 1, column_span=1)
    health_tile.create_tile()
    finance_tile = app_tile(frame, info_frame, 3, 0, 10, "Finance", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: app_tile.subtitle(finance_tile), 'dark slate grey', 'navajo white', 
                            'navajo white', 1, column_span=1)
    finance_tile.create_tile()
    calender_tile = app_tile(frame, info_frame, 4, 0, 10, "Calender", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: app_tile.subtitle(calender_tile), 'dark slate grey', 'navajo white', 
                            'navajo white', 1, column_span=1)
    calender_tile.create_tile()


def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time.config(text=current_time)
    current_date = datetime.now().strftime('%Y-%m-%d')
    date.config(text=current_date)
    window.after(1000, update_time)


def blank_page():
    global date, time, window, frame, info_frame

    window = tk.Tk()
    window.title("Rolodex.V1")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")
    window.configure(bg='dark slate grey')
    window.iconbitmap('Rolodex_icon.ico')

    logo = Image.open("Rolodex_logo.png").resize((80, 80))
    logo_image = ImageTk.PhotoImage(logo)
    border_thickness = 3
    canvas = tk.Canvas(window, width=logo.width + 2 * border_thickness, height=logo.height + 2 * border_thickness,
                       bg='navajo white', bd=0, highlightthickness=0)
    canvas.create_image((logo.width + 2 * border_thickness) / 2, (logo.height + 2 * border_thickness) / 2,
                        image=logo_image)
    canvas.grid(row=0, column=4, sticky="e")

    window.grid_rowconfigure(0, weight=0)  # title's row
    window.grid_rowconfigure(1, weight=1, minsize= 10)  # canvas's row
    window.grid_columnconfigure(0, weight=0)  # canvas's column
    window.grid_columnconfigure(1, weight=1)  # canvas's column

    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', 
                     font=("Lucida Sans Typewriter", 50))
    title.grid(row=0, column=1, sticky="w")

    frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    frame.grid(row=1, column=0, sticky="nsew", columnspan=1)
    frame.grid_columnconfigure(0, minsize=10, weight=0)

    info_frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    info_frame.grid(row=1, column=1, sticky="nsew", columnspan=4)
    info_frame.grid_columnconfigure(0, weight=1) 


    date_time_frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    date_time_frame.grid(row=0, column=3, sticky="nsew", columnspan=1)
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    date = tk.Label(date_time_frame, text=current_date, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    time = tk.Label(date_time_frame, text=current_time, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    date.grid(row=0, column=0, sticky='se', padx=10)
    time.grid(row=1, column=0, sticky='se', padx=10)

    home_setup(frame)

    def on_closing():
        window.destroy() 

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

    update_time()

    window.mainloop()


#blank_page()
