class BankAccount:

    num = 1

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.accountnumber = BankAccount.num
        BankAccount.num += 1

    def deposit(self, addition):
        self.balance += addition

    def getBalance(self):
        # return f'${self.balance}.00'
        return f'${self.balance:.2f}'
    
    def withdraw(self, removal):
        if self.balance - removal > 0:
            self.balance -= removal
        else:
            raise ValueError