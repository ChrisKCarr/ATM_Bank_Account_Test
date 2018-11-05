class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    
    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

chris_checking=Checking("account\\chris.txt", 1)
chris_checking.transfer(100)
print(chris_checking.balance)
chris_checking.commit()

mike_checking=Checking("account\\mike.txt", 1)
mike_checking.transfer(100)
print(mike_checking.balance)
mike_checking.commit()
