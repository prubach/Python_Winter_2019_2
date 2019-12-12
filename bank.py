class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __str__(self):
        return "Customer[{0},{1},{2}]".format(self.customer_id, self.first_name, self.last_name)

class Account:
    last_id = 0
    interest_rate = 0.001
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.account_id = Account.last_id
        self._balance = 0
    def deposit(self, amount):
        if amount>0:
            self._balance += amount
        else:
            raise BankException('Negative amount')
    def charge(self, amount):
        if amount < 0:
            raise NegativeAmountException()
        if amount > self._balance:
            raise NotEnoughMoneyException()
        self._balance -= amount
    def calc_interest(self):
        self._balance += self._balance * self.interest_rate
    def get_balance(self):
        return self._balance

    def __str__(self):
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, self.account_id, self._balance, self.customer.last_name)

class BankException(Exception):
    pass
class NegativeAmountException(BankException):
    pass
class NotEnoughMoneyException(BankException):
    pass

c1 = Customer("Anne","Smith","anne@smith.com")
a1 = Account(c1)
c2 = Customer("John", "Brown","john@brown.com")
print(c1)
print(a1)
try:
    a1.deposit(100)
    print(a1)
    a1.charge(150)
except NotEnoughMoneyException as ne:
    print("Not enough money")
    print(ne)
except NegativeAmountException as na:
    print("not enough money")
    print(na)
#except BankException as be:
    #print('Error: ' + str(be))
#res = a1.charge(150)
#print("result of charge {}".format(res))
print(a1)
a1.calc_interest()
print(a1)
#print(c2)
