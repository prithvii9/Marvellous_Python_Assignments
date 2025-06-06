class BankAccount : 
    ROI = 10.5

    def __init__(self):
        print("Name : ")
        self.Name = input()
        print("Amount : ")
        self.Amount = int(input())
        
    def Deposit(self, Amt):
        self.Amount = self.Amount + Amt
        print(Amt, " Deposited successfully!")
        

    def Withdraw(self, Amt):
        if(self.Amount < Amt):
            print("Insufficient Balance")
            return
        self.Amount = self.Amount - Amt
        print(Amt, " Withdrawn successfully!")

    def CalculateInterest(self):
        Ans = 0.0
        Ans = (self.Amount * BankAccount.ROI * 10) / 100
        return Ans

    
    def Display(self):
        print("Name of the Account Holder : ", self.Name)
        print("Available Balance : ", self.Amount)
        

def main():
    obj1 = BankAccount()
    obj1.Display()
    obj1.Deposit(1000)
    obj1.Display()
    obj1.Withdraw(500)
    obj1.Display()


if __name__ == "__main__":
    main()