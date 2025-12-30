# Simple class logic

class BankAccount:
    def __init__(self, owener_name, initial_balance):
        self.bank_name= "Global Bank"
        self.owner_name= owener_name
        self.balance= initial_balance

    def deposit(self, amount):
        self.balance += amount
        print (f"The new balance is {self.balance}")

    def withdraw(self, amount):
        if (amount > self.balance):
            print ("Cannot be Withdrawn!\nThe amount is greater than the balance.")
            print (self.balance)
        else:
            self.balance -= amount
            print (f"The new balance is {self.balance}")
    
    def __str__(self):
        return f"The owner name: {self.owner_name}\nThe bank name: {self.bank_name}\nThe balance: {self.balance}"
    
acc= BankAccount("Sreeja", 1000)
acc.deposit (300)
acc.withdraw(9000)
acc.withdraw(900)
print (acc)
