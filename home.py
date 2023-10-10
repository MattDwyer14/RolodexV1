import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image


class app_tile:

    def __init__(self, frame, row, column, width, text, font, function, background_colour, text_colour,
                 highlight_background, highlight_thickness):

        self.frame = frame
        self.row = row
        self.column = column
        self.width = width
        self.text = text
        self.font = font
        self.function = function
        self.background = background_colour
        self.text_colour = text_colour
        self.highlight_background = highlight_background
        self.highlight_thickness = highlight_thickness

    def create_tile(self):
        tile = tk.Button(self.frame, text=self.text, bg=self.background, fg=self.text_colour, font=self.font,
                         highlightbackground=self.highlight_background, highlightthickness=self.highlight_thickness,
                         command=self.function, width=self.width)
        tile.grid(row=self.row, column=self.column)


def subtitle(app_tile_instance):
    subtitle = tk.Label(text=app_tile_instance.text, bg='dark slate grey', fg='navajo white',
                        font=("Lucida Sans Typewriter", 15))
    subtitle.grid(row=0, column=1, sticky="sw")


def home_setup(frame):
    journal_tile = app_tile(frame, 0, 0, 10, "Journal", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: subtitle(journal_tile), 'dark slate grey', 'navajo white', 'navajo white', 1)
    journal_tile.create_tile()
    network_tile = app_tile(frame, 1, 0, 10, "Network", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: subtitle(network_tile), 'dark slate grey', 'navajo white', 'navajo white', 1)
    network_tile.create_tile()
    health_tile = app_tile(frame, 2, 0, 10, "Health", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: subtitle(health_tile), 'dark slate grey', 'navajo white', 'navajo white', 1)
    health_tile.create_tile()
    finance_tile = app_tile(frame, 3, 0, 10, "Finance", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: subtitle(finance_tile), 'dark slate grey', 'navajo white', 'navajo white', 1)
    finance_tile.create_tile()
    calender_tile = app_tile(frame, 4, 0, 10, "Calender", ("Lucida Sans Typewriter", 16, 'bold'),
                            lambda: subtitle(calender_tile), 'dark slate grey', 'navajo white', 'navajo white', 1)
    calender_tile.create_tile()


def update_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time.config(text=current_time)
    window.after(1000, update_time)


def blank_page():
    global date_time, window, frame

    window = tk.Tk()
    window.title("Rolodex.V1")
    window.geometry('750x550')
    window.configure(bg='dark slate grey')
    window.iconbitmap('Rolodex_icon.ico')

    logo = Image.open("Rolodex_logo.png")
    logo_resized = logo.resize((65, 65))
    logo_image = ImageTk.PhotoImage(logo_resized)
    logo_label = tk.Label(image=logo_image, highlightthickness=0, highlightbackground='navajo white')

    window.grid_rowconfigure(0, weight=0)  # title's row
    window.grid_rowconfigure(1, weight=1)  # canvas's row
    window.grid_columnconfigure(0, weight=0)# canvas's column
    window.grid_columnconfigure(1, weight=1)# canvas's column

    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 40))
    title.grid(row=0, column=0, sticky="sw")

    frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    frame.grid(row=1, column=0, sticky="nsew", columnspan=4)

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time = tk.Label(text=current_time, bg='dark slate grey', fg='navajo white',
                         font=("Lucida Sans Typewriter", 15))
    date_time.grid(row=0, column=2, sticky='se', padx=10)
    logo_label.grid(row=0, column=3, sticky="e")

    home_setup(frame)

    frame.grid_rowconfigure(1, weight=0)  # edit weights once rest of page design is finished
    frame.grid_columnconfigure(0, weight=0)

    update_time()

    window.mainloop()


blank_page()
