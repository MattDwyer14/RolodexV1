import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image


class app_tile:

    def __init__(self, row, column, width, text, font, function, background_colour, text_colour, highlight_background,
                 highlight_thickness):

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
        tile = tk.Button(frame, text=self.text, bg=self.background, fg=self.text_colour, font=self.font,
                         highlightbackground=self.highlight_background, highlightthickness=self.highlight_thickness,
                         command=self.function, width=self.width)
        tile.grid(row=self.row, column=self.column)


def update_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time.config(text=current_time)
    window.after(1000, update_time)


def journal_page():
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
    logo_label.grid(row=0, column=3, sticky="e")

    window.grid_rowconfigure(0, weight=0)  # title's row
    window.grid_rowconfigure(1, weight=1)  # canvas's row
    window.grid_columnconfigure(0, weight=1)  # canvas's column

    title = tk.Label(text="RolodexV1", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 40))
    title.grid(row=0, column=0, sticky="sw")

    subtitle = tk.Label(text="Journal", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 20))
    subtitle.grid(row=0, column=1, sticky="sw")

    frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    frame.grid(row=1, column=0, sticky="nsew", columnspan=4)

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time = tk.Label(text=current_time, bg='dark slate grey', fg='navajo white', font=("Arial", 16))
    date_time.grid(row=0, column=2, sticky='sw', padx=30)


    frame.grid_rowconfigure(1, weight=0)  # edit weights once rest of page design is finished
    frame.grid_columnconfigure(0, weight=0)

    update_time()

    window.mainloop()

window()
