class BankAccount:
    bank_name = "Bank of India"

    def __init__(self,account_holder,bank_balance):
        self.account_holder = account_holder
        self.bank_balance = bank_balance

    @classmethod

    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
    
    def display_account(self):
        print("Account Holder:",self.account_holder)
        print("Bank Balance:",self.bank_balance)
        print("Bank:",BankAccount.bank_name)

acc1 = BankAccount("Viraj",56000)
acc2 = BankAccount("Ayush",26534)

acc1.display_account()
acc2.display_account()

BankAccount.change_bank_name("State Bank of India")

print("After changing the Bank Name:")
acc1.display_account()
acc2.display_account()

