import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext 
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

def bring_frame_to_front(frame):
    frame.lift()

def clear_frame_entries(canvas):
    canvas.delete('all')

def add_entry_mode():
    global entry_frame_submit
    
    bring_frame_to_front(entry_frame_submit)

    # entry box for name and its corresponing label
    entry_name_label = tk.Label(entry_frame_submit, text="Entry Name: ", bg='dark slate grey', fg='navajo white', 
                                font=("Lucida Sans Typewriter", 15))
    entry_name_label.grid(row=0, column=0, sticky='ne', pady=5)

    entry_name =  tk.Entry(entry_frame_submit, width= 50, bg='dark slate grey', fg='navajo white', 
                           font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                           highlightthickness=3)
    entry_name.grid(row=0, column=1, sticky='w', pady=5)

    # entry box for entry body and its corresponding label
    entry_label = tk.Label(entry_frame_submit, text="Entry: ", bg='dark slate grey', fg='navajo white', 
                                font=("Lucida Sans Typewriter", 15))
    entry_label.grid(row=1, column=0, sticky='ne', pady=5)

    entry =  tk.scrolledtext.ScrolledText(entry_frame_submit, width=90, height=18, bg='dark slate grey', fg='navajo white', 
                      font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                      highlightthickness=3)
    entry.grid(row=1, column=1, sticky='nw', pady=5)

    
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    date_time = f"{current_date} {current_time}"
    
    def submit():
        if entry.get("1.0", "end-1c") == "":
            tk.messagebox.showerror(title="Error", message="Entry cannot be blank")
        
        if entry_name.get() == "":
            tk.messagebox.showerror(title="Error", message="Entry name cannot be blank")

        else:
            entry_text = entry.get("1.0", "end-1c")
            entry_name_text = entry_name.get()
            submit_entry(entry_name_text, date_time, entry_text)
            entry_name.delete(0, tk.END)
            entry.delete(1.0, tk.END)
    

    # submit button
    submit_button = tk.Button(entry_frame_submit, text="Submit", bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15), command = submit)
    submit_button.grid(row=2, column=1, sticky='nw', pady=5)

def fetch():
    global entry_canvas, entry_frame_view

    bring_frame_to_front(entry_frame_view)
    clear_frame_entries(entry_canvas)
    entries = fetch_entries_from_db()
    
    if entries == []:
        pass
    else:
        label_height = 0
        for entry in reversed(entries):
            print_entries = ''
            split_date_time = entry[0].split()
            date_split = split_date_time[0]
            date = "".join(date_split)
            time_split = split_date_time[1]
            time = "".join(time_split)
            print_entries = f'Date: {date} \nTime: {time} \nEntry ID: {entry[3]} \nName: {entry[1]} \n\n{entry[2]}\n'

            entry_label = tk.Label(entry_frame_view, text=print_entries, bg='dark slate grey', fg='navajo white', 
                        font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                        highlightthickness=3, width=110, wraplength=1000, justify="left", anchor = 'w')
            entry_canvas.create_window(0, label_height, window=entry_label, anchor="nw")
            label_height += entry_label.winfo_reqheight()
    entry_canvas.config(scrollregion=entry_canvas.bbox("all"))

def delete():
    global delete_id_entry
    delete_id = delete_id_entry.get()
    delete_entry(delete_id)
    delete_id_entry.delete(0, tk.END)
    fetch()
 


def blank_page():
    global time, date, window, entry_frame_submit, delete_id_entry, entry_canvas, entry_frame_view
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

    entry_frame_submit = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', 
                               highlightthickness=3)
    entry_frame_submit.grid(row=2, column=0, columnspan=4, sticky='nsew', pady=5)

    entry_frame_view = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', 
                               highlightthickness=3)
    entry_frame_view.grid(row=2, column=0, columnspan=4, sticky='nsew', pady=5)
    
    #create scrollbar entry_view_frame
    scrollbar = tk.Scrollbar(entry_frame_view, orient=tk.VERTICAL)
    # Attach the scrollbar to the frame
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Create a canvas to contain the labels
    entry_canvas = tk.Canvas(entry_frame_view, yscrollcommand=scrollbar.set, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=0)
    entry_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # Configure the scrollbar to control the canvas
    scrollbar.config(command=entry_canvas.yview)
  
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

    #title for program
    title = tk.Label(text="Rolodex.V1", bg='dark slate grey', fg='navajo white', 
                     font=("Lucida Sans Typewriter", 50))
    title.grid(row=0, column=0, columnspan=1, sticky="w")

    #defining date and time and positioning label
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')

    date_time_frame = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    date_time_frame.grid(row=0, column=2, sticky="nsw", columnspan=1)

    date = tk.Label(date_time_frame, text=current_date, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    time = tk.Label(date_time_frame, text=current_time, bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    
    date.grid(row=0, column=0, sticky='se', padx=10)
    time.grid(row=1, column=0, sticky='se', padx=10)

    journal_tile = tk.Frame(window, bg="dark slate grey", highlightbackground='navajo white', highlightthickness=3)
    journal_tile.grid(row=1, column=0, sticky="nsw", columnspan=4)

    #creates add entry button
    add_entry = tk.Button(journal_tile, text="Add Entry", bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15), command=add_entry_mode)
    add_entry.grid(row=0, column=1, sticky='nesw')

    #show entries button
    show_entries = tk.Button(journal_tile, text="Show Entries", bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15), command=fetch)
    show_entries.grid(row=0, column=0, sticky='nesw')

    #delete entries entry box
    delete_label = tk.Label(journal_tile, text="Delete Entry: ", bg='dark slate grey', fg='navajo white',
                    font=("Lucida Sans Typewriter", 15))
    delete_label.grid(row=0, column=2, sticky='nesw')
    delete_id_entry =  tk.Entry(journal_tile, width= 10, bg='navajo white', fg='dark slate grey',
                           font=("Lucida Sans Typewriter", 15), highlightbackground='navajo white', 
                           highlightthickness=3)
    delete_id_entry.grid(row=0, column=3, sticky='w', pady=5)
    
    delete_button = tk.Button(journal_tile, text="Confirm", bg='dark slate grey', fg='navajo white', 
                              font=("Lucida Sans Typewriter", 15), command=delete)
    delete_button.grid(row=0, column=4, sticky='nesw')


    def on_closing():
        window.destroy()
        exit()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    fetch()

    update_time()

    window.mainloop()


blank_page()
