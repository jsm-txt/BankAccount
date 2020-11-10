from random import randint

class BankAccount:
    routing_number = 123456789

    def __init__(self, name):
        self._name = name
        self._account_number = randint(10000000,19999999)
        self._balance = 0

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
        account = self._account_number
        account = account % 10000
        routing_number =0

        print(f'{self._name}')
        print(f'Account No.: ****{account}')
        print(f'Routing No.: {BankAccount.routing_number}')
        print(f'Balance: ${"{:.2f}".format(self._balance)}')
        return 


jj = BankAccount('JJ')
jj.deposit(200)
jj.withdraw(500)
jj.withdraw(100)
jj.get_balance()
jj.add_interest()
jj.get_balance()
jj.print_receipt()

aa = BankAccount( 'Aa')
aa.deposit(300)
aa.withdraw(1300)
aa.get_balance()
aa.add_interest()
aa.print_receipt()

dd = BankAccount('DD')
dd.deposit(500)
dd.withdraw(1000)
dd.withdraw(100)
dd.get_balance()
dd.add_interest()
dd.print_receipt()
