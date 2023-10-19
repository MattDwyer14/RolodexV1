import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image

def update_time():
    global time, date, window
    current_time = datetime.now().strftime('%H:%M:%S')
    time.config(text=current_time)
    current_date = datetime.now().strftime('%Y-%m-%d')
    date.config(text=current_date)
    window.after(1000, update_time)

def blank_page():
    global time, date, window
    #creates window for the home
    window = tk.Tk()
    window.title("Rolodex.V1")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")
    window.configure(bg='dark slate grey')
    window.iconbitmap('Rolodex_icon.ico')

    #loading logo image from program files
    logo = Image.open("Rolodex_logo.png").resize((80, 80))
    logo_image = ImageTk.PhotoImage(logo)
    border_thickness = 3

    #cancas for logo image. canvas' are better for laying images
    canvas = tk.Canvas(window, width=logo.width + 2 * border_thickness, height=logo.height + 2 * border_thickness,
                       bg='navajo white', bd=0, highlightthickness=0)
    canvas.create_image((logo.width + 2 * border_thickness) / 2, (logo.height + 2 * border_thickness) / 2,
                        image=logo_image)
    canvas.grid(row=0, column=4, sticky="e")

    #window size configuration
    window.grid_rowconfigure(0, weight=0)  # title's row
    window.grid_rowconfigure(1, weight=1, minsize= 10)  # canvas's row
    window.grid_columnconfigure(0, weight=0)  # canvas's column
    window.grid_columnconfigure(1, weight=1)  # canvas's column

    #title for program
    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', 
                     font=("Lucida Sans Typewriter", 50))
    title.grid(row=0, column=1, sticky="w")

    #defining date and time and positioning label
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

    def on_closing():
        exit()

    window.protocol("WM_DELETE_WINDOW", on_closing)


    update_time()

    window.mainloop()


blank_page()
