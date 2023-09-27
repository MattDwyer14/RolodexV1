import tkinter as tk


def home_page():
    homepage = tk.Tk()
    homepage.title("Rolodex.V1")
    homepage.geometry('750x550')
    homepage.configure(bg='dark slate grey')

    def toggle_fullscreen():
        state = not homepage.attributes('-fullscreen')
        homepage.attributes('-fullscreen', state)
        return "break"

    # Uncomment if you want the fullscreen toggle feature
    # homepage.attributes('-fullscreen', True)
    # homepage.bind("<Escape>", toggle_fullscreen)

    # Setting weights for rows and columns
    homepage.grid_rowconfigure(0, weight=1)  # title's row
    homepage.grid_rowconfigure(1, weight=5)  # canvas's row
    homepage.grid_columnconfigure(0, weight=1)  # canvas's column

    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', font=("Lucida Sans Typewriter", 30))
    title.grid(row=0, column=0, sticky="nw")

    # Create a canvas for drawing
    canvas = tk.Canvas(homepage, bg="blue")
    canvas.grid(row=1, column=0, sticky="nsew")

    homepage.mainloop()


home_page()


home_page()






