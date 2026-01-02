import sqlite3

conn = sqlite3.connect("database.db" , check_same_thread= False)

cursor = conn.cursor()



cursor.execute("""CREATE TABLE IF NOT EXISTS bookings
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               phone TEXT NOT NULL,
               service TEXT NOT NULL,
               date TEXT NOT NULL, 
               time TEXT NOT NULL,
               instructions TEXT
               )
               """)

def add_booking(name , phone , service, date , time , instructions):
    cursor.execute("""
    INSERT INTO bookings(name , phone ,service , date, time , instructions)
    VALUES(? , ? , ? , ? , ?, ?)""",
    (name , phone , service , date , time , instructions))


    conn.commit()
    # conn.close()




conn.commit()
