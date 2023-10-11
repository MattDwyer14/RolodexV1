import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image

class journal_tile:

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

def new_entry(frame):
    entry = journal_tile(frame, 0, 2, 10, datetime.now().strftime('%H:%M:%S'), ("Lucida Sans Typewriter", 16, 'bold'), new_entry
                         , 'dark slate grey', 'navajo white', 'navajo white', 1)

def launch_journal(frame):
    add_entry = journal_tile(frame, 0, 2, 10, "Add Entry", ("Lucida Sans Typewriter", 16, 'bold'), new_entry
                         , 'dark slate grey', 'navajo white', 'navajo white', 1)
    add_entry.create_tile()

