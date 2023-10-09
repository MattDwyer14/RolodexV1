import tkinter as tk

root = tk.Tk()
root.title("Learning Page")
root.geometry('500x350')


def add_name():
    name_input = entry_1.get()
    new_label = tk.Label(root, text=name_input)
    new_label.pack()

label_1 = tk.Label(root, text='name gallery', font=('Arial', 60))
label_1.pack()

button_1 = tk.Button(text='click to add name',  command=add_name)
button_1.pack()

entry_1 = tk.Entry(root, bg='white', fg='black')
entry_1.pack()

root.mainloop()

