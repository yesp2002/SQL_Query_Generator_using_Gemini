import sqlite3

##Connect to sqlite
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

### Insert Some more records

cursor.execute('''Insert into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Sudanshu', 'Data Science', 'B', 100)''')
cursor.execute('''Insert into STUDENT values('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''Insert into STUDENT values('Vikash', 'Devops', 'A', 90)''')

print("The inserted records are")

data = cursor.execute('''Select * FROM STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()



