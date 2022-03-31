
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Manager job....")

class Developer(Employee):
    def doJob(self):
        print("Developer Job....")

def BankFun(emp):
    print("BankjobStarted".center(40, "-"))
    emp.doJob()
    print("BankjobEnded".center(40, "-"))
    print("-" * 40)

Moses = Manager()
David = Developer()

BankFun(Moses)
BankFun(David)

print("-" * 40)
def BankFunJobs(emps):
    print("BankjobStarted".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("BankjobEnded".center(40, "-"))
    print("-" * 40)

BankFunJobs([Moses, David])
