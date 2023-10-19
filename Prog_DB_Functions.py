#functions in this file will be used by the program 
#to interact with the database

import sqlite3
from DB_Setup import *

def submit(entry_name, entry):
    conn = sqlite3.connect('journal.db')
    #create cursor to interact with database
    c = conn.cursor()

    c.execute('''
        INSERT
    ''')

    #commit changes to databases after every change
    conn.commit()
    #close connection when finished
    conn.close()