
import sqlite3

conn = sqlite3.connect("emp.sqlite3")

cursor = conn.cursor()

query = """
create table emp (
empid char(5) PRIMARY KEY,  
empname char(50) not null,
desig char(30) not null,
dept char(30) not null,
salary real not null
)
"""
cursor.execute(query)

conn.close()
