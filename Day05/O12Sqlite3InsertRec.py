
import sqlite3

conn = sqlite3.connect("emp.sqlite3")

cursor = conn.cursor()

query = """
insert into emp values ("EMP50", "Jane", "TL", "PROC", 90000)
"""
cursor.execute(query)

conn.commit()

conn.close()