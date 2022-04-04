
import pymysql
from prettytable import PrettyTable

conn = pymysql.connect(host="localhost", user="root", password="", database="employees", port=3306)

cursor = conn.cursor()

query = "select * from emp"

cursor.execute(query)

pt = PrettyTable()

pt.field_names = ["EMPID", "EMPNAME", "DESIGNATION", "DEPARTMENT", "SALARY"]
pt.align['EMPNAME'] = "l"
pt.align['DESIGNATION'] = "l"
pt.align["SALARY"] = "r"

pt.sortby = "SALARY"
# pt.reversesort = True

for row in cursor.fetchall():
    pt.add_row(row)

conn.close()

print(pt)