class BankAccount:

    def __init__(self, name, account_number, routing_number, balance):
        self._name = name
        self._account_number = account_number
        self._routing_number = routing_number 
        self._balance = balance


    def deposit(self, amount):
        self._balance = amount + self._balance
        return print(f'Amount Deposited: ${amount}')

    def withdraw(amount):
        pass

    def get_balance():
        pass

    def add_interest():
        pass

    def print_receipt():
        pass


jj = BankAccount('JJ',100000000,123456789, 200)
jj.deposit(200)
