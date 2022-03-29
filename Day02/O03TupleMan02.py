
from collections import namedtuple

nmdTpl = namedtuple("Employee", "ename age salary dept")
emp = nmdTpl(ename="Louis", age=29, salary=58000, dept='mkt')
print(f"emp :{emp}")
print(f"Name   :{emp.ename}")
print(f"Age    :{emp.age}")
print(f"Salary :{emp.salary}")
print(f"Dept   :{emp.dept}")

emp.age = 32
