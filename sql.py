import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

## Create the table
table_info = """
            Create table STUDENT(NAME VARCHAR(25), 
                                CLASS VARCHAR(25),
                                SECTION VARCHAR(25),
                                MARKS INT);
            """

cursor.execute(table_info)


## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish', 'Data SCience', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Susovan', 'Data SCience', 'B', 80)''')
cursor.execute('''Insert Into STUDENT values('Sarath', 'Image Processing', 'A', 100)''')
cursor.execute('''Insert Into STUDENT values('Ritika', 'Excel', 'A', 95)''')
cursor.execute('''Insert Into STUDENT values('Ayush', 'Data SCience', 'C', 70)''')


## Display all the records
print(" The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)


## CLose the connection
connection.commit()
connection.close()









