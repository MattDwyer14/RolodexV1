import tkinter as tk
from datetime import datetime
from PIL import ImageTk,Image


def update_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time.config(text=current_time)
    print("time")
    homepage.after(1000, update_time)


def home_page():
    global date_time, homepage

    homepage = tk.Tk()
    homepage.title("Rolodex.V1")
    homepage.geometry('750x550')
    homepage.configure(bg='dark slate grey')
    homepage.iconbitmap('Rolodex_icon.ico')

    logo = Image.open("Rolodex_logo.png")
    logo_resized = logo.resize((65, 65))
    logo_image = ImageTk.PhotoImage(logo_resized)
    logo_label = tk.Label(image=logo_image, highlightthickness=0, highlightbackground='navajo white')

    homepage.grid_rowconfigure(0, weight=0)  # title's row
    homepage.grid_rowconfigure(1, weight=1)  # canvas's row
    homepage.grid_columnconfigure(0, weight=1)  # canvas's column

    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 40))
    title.grid(row=0, column=0, sticky="sw")

    frame = tk.Frame(homepage, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    frame.grid(row=1, column=0, sticky="nsew", columnspan=3)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_time = tk.Label(text=current_time, bg='dark slate grey', fg='navajo white', font=("Arial", 16))
    date_time.grid(row=0, column=1, sticky='sw',padx=30)
    logo_label.grid(row=0, column=2, sticky="e")

    update_time()

    homepage.mainloop()

#home_page()