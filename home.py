import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
from Prog_DB_Functions import *

def update_time():
    global time, date, window
    current_time = datetime.now().strftime('%H:%M:%S')
    time.config(text=current_time)
    current_date = datetime.now().strftime('%Y-%m-%d')
    date.config(text=current_date)
    window.after(1000, update_time)

def add_entry_mode():
    global entry_frame

    #remove all other widgets except top row here

    entry_name_label = tk.Label(entry_frame, text="Entry Name: ", bg='dark slate grey', fg='navajo white', 
                                font=("Lucida Sans Typewriter", 15))
    entry_name_label.grid(row=0, column=0, sticky='ne')
    entry_name =  tk.Entry(entry_frame, width= 50, bg='dark slate grey', fg='navajo white', 
                           font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                           highlightthickness=3)
    entry_name.grid(row=0, column=1, sticky='w')

    entry_label = tk.Label(entry_frame, text="Entry: ", bg='dark slate grey', fg='navajo white', 
                                font=("Lucida Sans Typewriter", 15))
    entry_label.grid(row=1, column=0, sticky='ne')
    entry =  tk.Text(entry_frame, width=90, height=15, bg='dark slate grey', fg='navajo white', 
                      font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                      highlightthickness=3)
    entry.grid(row=1, column=1, sticky='nw')

def blank_page():
    global time, date, window, entry_frame
    #creates window for the home
    window = tk.Tk()
    window.title("Rolodex.V1")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")
    window.configure(bg='dark slate grey')
    window.iconbitmap('Rolodex_icon.ico')

    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)

    entry_frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', 
                               highlightthickness=3)
    entry_frame.grid(row=2, column=0, columnspan=4, sticky='nsew')

    #loading logo image from program files
    logo = Image.open("Rolodex_logo.png").resize((80, 80))
    logo_image = ImageTk.PhotoImage(logo)
    border_thickness = 3

    #cancas for logo image. canvas' are better for laying images
    canvas = tk.Canvas(window, width=logo.width + 2 * border_thickness, height=logo.height + 2 * border_thickness,
                       bg='navajo white', bd=0, highlightthickness=0)
    canvas.create_image((logo.width + 2 * border_thickness) / 2, (logo.height + 2 * border_thickness) / 2,
                        image=logo_image)
    canvas.grid(row=0, column=3, sticky="e")
    filler_frame = tk.Frame(window, highlightthickness=0)
    filler_frame.grid(row=0, column=1, columnspan=2)

    #title for program
    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', 
                     font=("Lucida Sans Typewriter", 50))
    title.grid(row=0, column=0, columnspan=1, sticky="w")

    #defining date and time and positioning label
    date_time_frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    date_time_frame.grid(row=0, column=2, sticky="nsw", columnspan=1)
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    date = tk.Label(date_time_frame, text=current_date, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    time = tk.Label(date_time_frame, text=current_time, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    date.grid(row=0, column=0, sticky='se', padx=10)
    time.grid(row=1, column=0, sticky='se', padx=10)

    #creates add entry button
    add_entry = tk.Button(window, text="Add Entry", bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15), command=add_entry_mode)
    add_entry.grid(row=1, column=0, sticky='nw')


    def on_closing():
        window.destroy()
        exit()

    window.protocol("WM_DELETE_WINDOW", on_closing)


    update_time()

    window.mainloop()


blank_page()
