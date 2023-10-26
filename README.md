# RolodexV1
RolodexV1 is intended as a learning environment for me to practice working with a database and 
get to grips with new GUI tools. The first iteration will be implementing a journal app that can be used to write long text and save it to the database with information on the date and time it was written. the user will then be able to scroll through all the entries and delete entries based on the unique primary key that all entries are assigned. all of this is implemented through the GUI and is intended to be very simple to use.

the next iteration will add more functionality in the form of a contact book that can be filtered in useful ways and then also health metrics that will use matplotlib graphs to track various data and assist in idetifying health trends.

the application uses sqlite3 which comes with python and is made using the tkinter package. to use the program first run the DB_Setup file to create the Rolodex.db database and then run the main.py to launch the program. 

username and password are both set to "a" currently however password hashing will be implemented later on as it seems like it would be fun to try.