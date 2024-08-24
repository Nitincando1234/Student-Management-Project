import sqlite3
def create_db():
    con = sqlite3.connect(database = "rms.db")          # rms.db for result management system
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, charges TEXT, description TEXT)")
    con.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY,name TEXT, email TEXT, gender TEXT, dob TEXT, contact TEXT, admission TEXT, course TEXT, state TEXT, city TEXT, pin TEXT, address TEXT)")
    con.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll TEXT, name TEXT, course TEXT, marks_ob TEXT, fullmarks TEXT, per TEXT)")
    con.commit()

    con.close()
create_db()
    