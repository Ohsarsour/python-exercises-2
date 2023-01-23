from BankAccount import BankAccount
account=BankAccount("Wally",2500)
account.deposit(800)
account.withdraw(450)
print(account.get_balance())