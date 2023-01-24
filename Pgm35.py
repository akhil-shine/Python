class bank:
    def __init__(self,account_number,name,type_of_account):
        self.account_number=account_number
        self.name=name
        self.type_of_account=type_of_account
        self.bal=0


    def showamt(self):
        print("Account holder name:", self.name)
        print("Account Number:", self.account_number)
        print("Account type:", self.type_of_account)
        print("Your balance is:", self.bal)

    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal

    def wdraw(self, w1):
        self.bal = self.bal - w1
        return self.bal

a=input("Enter your Name:")
b=int(input("Enter your Account No:"))
c=input("Enter you account type:")
y=0
e=bank(a,b,c)
e.showamt()
while(True):
    print("\nMENU")
    print("1.Deposit")
    print("2.Withdraw")
    d=int(input("Enter you choice:"))
    if (d==1):
        y=int(input("Enter the amount to deposit:"))
        print("Your Total Balance is:",e.dep(y))
    elif(d==2):
        w=int(input("Enter the amount to be withdraw:"))
        if(w>y):
            print("Insuffient Balance")
        else:
            print("Your total balance is:",e.wdraw(w))
    else:
        print("Enter a valid choice")


