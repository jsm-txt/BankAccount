class BankAccount:

    def __init__(self, name, account_number, routing_number, balance):
        self._name = name
        self._account_number = account_number
        self._routing_number = routing_number 
        self._balance = balance


    def deposit(self, amount):
        self._balance = amount + self._balance
        return print(f'Amount Deposited: ${amount}')

    def withdraw(self, amount):
        if amount > self._balance:
            self._balance = self._balance - 10
            print('Insufficient funds')
        else:
            self._balance = self._balance - amount
            return print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        balance = self._balance
        return print(f'Current Balance ${"{:.2f}".format(balance)}')

    def add_interest(self):
        interest = self._balance *  0.00083
        self._balance = self._balance +interest
        return 
    def print_receipt(self):
        account = 0
        print(f'{self._name}')
        print(f' Account No.: {account}')
        print(f'Routing No.: {self._routing_number}')
        print(f'Balance: ${"{:.2f}".format(self._balance)}')
        return 


jj = BankAccount('JJ',100000000,123456789, 200)
jj.deposit(200)
jj.withdraw(500)
jj.withdraw(100)
jj.get_balance()
jj.add_interest()
jj.get_balance()
jj.print_receipt()