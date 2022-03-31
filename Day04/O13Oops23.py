
# Duck types

class Manager:
    def doJob(self):
        print("Manager job....")

class Developer():
    def doJob1(self):
        print("Developer Job....")

Moses = Manager()
David = Developer()

def BankFunJobs(emps):
    print("BankjobStarted".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("BankjobEnded".center(40, "-"))
    print("-" * 40)

BankFunJobs([Moses, David])
