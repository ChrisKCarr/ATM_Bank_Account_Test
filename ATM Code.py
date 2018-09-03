
# coding: utf-8

class Account:
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance} '
    
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f'${dep_amt} was added into the account for {self.owner}')
        
    def withdraw(self,wit_amt):
        if self.balance >= wit_amt:
            self.balance -= wit_amt
            print(f'${wit_amt} was withdrawn from the account for {self.owner}')
        else:
            print(f'The account for {self.owner} does not have the required funds to make this withdrawl\nThe current balance is ${self.balance}')
        
