class BankAccount:

    num = 1

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountnumber = BankAccount.num
        BankAccount.num += 1

    def deposit(self, addition):
        self.balance += addition

    def getBalance(self):
        return f'${self.balance}.00'
    
    def withdraw(self, removal):
        if self.balance - removal > 0:
            self.balance -= removal
        else:
            raise ValueError