import tkinter as tk
from tkinter import messagebox


def login_page():
    global username_entry, password_entry, verified, home, window
    window = tk.Tk()
    window.title("Login")
    window.geometry('500x400')
    window.configure(bg='dark slate grey')

    frame = tk.Frame(bg='dark slate grey')
    login_label = tk.Label(frame, text="Login", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 30))
    username_label = tk.Label(frame, text="Username: ", bg='dark slate grey', fg="navajo white", font=("Lucida Sans Typewriter", 16, 'bold'))
    password_label = tk.Label(frame, text="Password: ", bg='dark slate grey', fg="navajo white", font=("Lucida Sans Typewriter", 16, 'bold'))
    username_entry = tk.Entry(frame, font=("Lucida Sans Typewriter", 16), bg='dark slate grey', fg="navajo white",
                              highlightbackground='navajo white', highlightthickness=2)
    password_entry = tk.Entry(frame, show="*", font=("Lucida Sans Typewriter", 16), bg='dark slate grey',
                              fg="navajo white", highlightbackground='navajo white', highlightthickness=2)
    login_button = tk.Button(frame, text="Login", bg="navajo white", fg="dark slate grey",
                             font=("Lucida Sans Typewriter", 20, 'bold'), highlightbackground='navajo white', highlightthickness=1, command=login)

    login_label.grid(row=0, column=0, columnspan=1, sticky="news", pady=30)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()
    window.mainloop()
    print(verified, "stage 2")
    return verified


def login():
    global username_entry, password_entry, verified, home, window
    username = "a"
    password = "a"
    if username_entry.get() == username and password_entry.get() == password:
        verified = True
        window.destroy()
        print(verified, "stage 1")
        return verified

    else:
        tk.messagebox.showerror(title="Error", message="Invalid login.")
