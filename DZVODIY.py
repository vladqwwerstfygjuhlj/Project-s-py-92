class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів.")

    def __str__(self):
        return f"Власник: {self.owner}, Номер рахунку: {self.account_number}, Баланс: {self.balance} грн"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
        else:
            print("Недостатньо коштів для переказу.")

    def show_accounts(self):
        for account in self.accounts:
            print(account)

account1 = BankAccount("Олена", "12345", 5000)
account2 = BankAccount("Іван", "67890", 3000)
bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.transfer(account1, account2, 1000)
bank.show_accounts()
