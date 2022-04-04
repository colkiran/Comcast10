
import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("emp.sqlite3")

cursor = conn.cursor()

query = "select * from emp"

cursor.execute(query)

pt = from_db_cursor(cursor)
pt.align['salary'] = 'r'
pt.align['empname'] = "l"
pt.align['desig'] = "l"
pt.align['dept'] = "l"

conn.close()

print(pt)
