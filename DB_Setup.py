import sqlite3


# this function only needs to be run once during setup to create the database
def database_setup():
    #step 1: create a database or connect to one
    conn = sqlite3.connect('journal.db')
    #create cursor to interact with database
    c = conn.cursor()
    
    #create table inside database
    c.execute("""
            CREATE TABLE journal (
              id INTEGER NOT NULL,
              date_time TEXT NOT NULL,
              entry_name TEXT NOT NULL,
              entry TEXT NOT NULL)
        """)
    
    
    #commit changes to databases after every change
    conn.commit()
    #close connection when finished
    conn.close()


#database_setup()

