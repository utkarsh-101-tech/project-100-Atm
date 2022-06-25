class Atm :
    def __init__(self,cardNo,pinNo) :
        self.cardNo = cardNo
        self.cardNo = pinNo
        self.balance = 95638000

    def cashWithdrawl(self) :
        cashtaken = int(input("enter the amount to withdraw --> "))
        self.balance = self.balance-cashtaken
        print("transaction successful \nbalance left in account --> " +str(self.balance))

    def balanceEnquiry(self) :
        print("balance left in account --> "+str(self.balance))

accNo = int(input("Enter your account number or cardNumber\n_"))
pinNo = int(input("Enter your pin\n_"))
myAcc = Atm(accNo,pinNo)

opt = int(input("for cash withdrawl press 1 \nfor balance enquiry press 2\n_"))
if opt==1 :
    myAcc.cashWithdrawl()
else : 
    myAcc.balanceEnquiry()