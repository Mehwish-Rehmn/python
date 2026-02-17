'''SQL = structured query language  
it is the language you use to talk to databases — ask questions, get data, add/update/delete records.

SQLITE = a very small, file-based database engine  
no server needed, just one file on your computer (like sales.db).  
perfect for learning, small apps, bootcamps, mobile apps, testing.

sqlite + sql = best combo to learn sql without installing big software.

 why sqlite is great for beginners

- no installation headache (built into python)
- everything saved in one .db file
- delete the file = delete database
- fast and zero configuration
'''
### how to use sqlite in python 
import sqlite3

# connect (creates file if not exists)
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

### step by step examples (run in order)

# CREATE LAB
cursor.execute("""
create table if not exists students (
    id integer primary key autoincrement,
    name text not null,
    age integer,
    city text
)
""")
conn.commit()


# INSERT DATA
cursor.execute("insert into students (name, age, city) values (?, ?, ?)", 
               ("alex", 20, "delhi"))

cursor.execute("insert into students (name, age, city) values (?, ?, ?)", 
               ("sara", 22, "mumbai"))

conn.commit()


#SELECT/READ DATA
cursor.execute("select * from students")
rows = cursor.fetchall()

for row in rows:
    print(row)  # (1, 'alex', 20, 'delhi') ...


# SELECT WITH WHERE
cursor.execute("select name, age from students where age > 21")
for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("update students set age = 23 where name = 'alex'")
conn.commit()

# DELETE
cursor.execute("delete from students where name = 'sara'")
conn.commit()

# DROP TABLE
cursor.execute("drop table if exists students")
conn.commit()


# CLOSE CONNECTION
conn.close()


### program 

import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists marks (
    id integer primary key autoincrement,
    student_name text,
    subject text,
    score integer
)
""")

# add some data
data = [
    ("riya", "math", 85),
    ("karan", "science", 92),
    ("riya", "english", 78)
]
cursor.executemany("insert into marks (student_name, subject, score) values (?, ?, ?)", data)

conn.commit()

# query
cursor.execute("select student_name, avg(score) from marks group by student_name")
for row in cursor.fetchall():
    print(f"{row[0]} average: {row[1]:.1f}")

conn.close()



## Working Wwith Sales Data
# Connect to an SQLite database
connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

# Create a table for sales data
cursor.execute("select * from sales")
for row in cursor.fetchall():
    print(row)
'''(
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT
)
'''

# Insert data into the sales table
sales_data = [
    ('2023-01-01', 'Product1', 30, 'North'),
    ('2023-01-02', 'Product2', 50, 'South'),
    ('2023-01-03', 'Product1', 60, 'East'),
    ('2023-01-04', 'Product3', 750, 'West'),
    ('2023-01-05', 'Product2', 390, 'North')
]

cursor.executemany('''
Insert into sales(date,product,sales,region)
                   values(?,?,?,?)
''',sales_data)

connection.commit()