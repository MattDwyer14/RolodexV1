import tkinter as tk
from tkinter import messagebox


def login_page():
    global username_entry, password_entry, verified, home, window
    window = tk.Tk()
    window.title("Login")
    window.geometry('500x400')
    window.configure(bg='#000000')

    frame = tk.Frame(bg='#000000')
    login_label = tk.Label(frame, text="Login", bg='#000000', fg='green2', font=("Arial", 30))
    username_label = tk.Label(frame, text="Username", bg='#000000', fg="green2", font=("Arial", 16, 'bold'))
    password_label = tk.Label(frame, text="Password", bg='#000000', fg="green2", font=("Arial", 16, 'bold'))
    username_entry = tk.Entry(frame, font=("Arial", 16), bg='#000000', fg="green2",
                              highlightbackground='green2', highlightthickness=2)
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16), bg='#000000', fg="green2",
                              highlightbackground='green2', highlightthickness=2)
    login_button = tk.Button(frame, text="Login", bg="#000000", fg="green2", font=("Arial", 16),
                             highlightbackground='green2', highlightthickness=3, command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
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
        tk.messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        verified = True
        window.destroy()
        print(verified, "stage 1")
        return verified

    else:
        tk.messagebox.showerror(title="Error", message="Invalid login.")
