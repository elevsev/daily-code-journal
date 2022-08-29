import sqlite3
sqliteConnection = sqlite3.connect('gfg.db')
cursor = sqliteConnection.cursor()

sql_command = '''CREATE TABLE emp (
        staff_number INTEGER PRIMARY KEY,
        fname VARCHAR (20),
        lname VARCHAR (20),
        gender CHAR (1),
        joining DATE
);
'''
cursor.execute(sql_command)

sql_command2 = """INSERT INTO emp VALUES (23, "Rishabh",\
"Bansal", "M", "2014-03-28");"""

cursor.execute(sql_command2)

sqliteConnection.commit()

for row in cursor:
    print(row)