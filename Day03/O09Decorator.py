

def Bankfun(fnc):

    def helperFun(amt):
        print("Logged into the system......")
        fnc(amt)
        print("logged out of the system.......")
        print("-" * 40)

    return helperFun

@Bankfun                # dpRef = Bankfun(deposit)
def deposit(amt):
    print(f"Amount {amt} credited into the account successfully....")

@Bankfun
def withDraw(amt):
    print(f"Amount {amt} debited from the account.....")

@Bankfun
def trasfer(amt):
    print(f"Amount {amt} transferred from the account.....")


deposit(50000)
withDraw(10000)
trasfer(5000)

