

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="employees", port=3306)

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
