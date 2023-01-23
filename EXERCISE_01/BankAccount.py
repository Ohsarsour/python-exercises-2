class BankAccount:
    #init constructor to initialize(assign values) to the data members of the class when an object is created
    def __init__(cust,account_name,starting_balance):
        cust.account_name=account_name
        cust.balance=starting_balance

    def deposit(cust,amount):
        cust.balance=cust.balance+amount

    def withdraw(cust,amount):
        # if balance is greater than or equal to the amount then withdraw
        if cust.balance>=amount:
            cust.balance=cust.balance-amount
        else:
            print("No sufficient balance to withdraw")

    def get_balance(cust):
        return str(cust.account_name)+" has a balance of $"+str(cust.balance)