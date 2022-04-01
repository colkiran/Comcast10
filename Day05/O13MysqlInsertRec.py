


import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="employees", port=3306)

cursor = conn.cursor()

query = """
insert into emp values ("EMP01", "Jack", "MGR", "HR", 85000)
"""
cursor.execute(query)

conn.close()
