#functions in this file will be used by the program 
#to interact with the database

import sqlite3

def submit_entry(entry_name, date_time, entry):
    conn = sqlite3.connect('Rolodex.db')
    #create cursor to interact with database
    c = conn.cursor()

    #insert entry info into table
    c.execute('''
        INSERT INTO journal (date_time, entry_name, entry)
        VALUES (?, ?, ?)
    ''', (date_time, entry_name, entry))

    #commit changes to databases after every change
    conn.commit()
    #close connection when finished
    conn.close()

def fetch_entries_from_db():
    conn = sqlite3.connect('Rolodex.db')
    #create cursor to interact with database
    c = conn.cursor()

    #fetch entry info into table
    c.execute('SELECT *, oid FROM journal')
    entries = c.fetchall()
    
    #commit changes to databases after every change
    conn.commit()
    #close connection when finished
    conn.close()
    return entries

def delete_entry(delete_id):
    conn = sqlite3.connect('Rolodex.db')
    #create cursor to interact with database
    c = conn.cursor()

    #fetch entry info into table
    c.execute("DELETE FROM journal WHERE oid=:entry_id", {'entry_id': delete_id})
    entries = c.fetchall()
    
    #commit changes to databases after every change
    conn.commit()
    #close connection when finished
    conn.close()

