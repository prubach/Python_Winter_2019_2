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
    #
    def charge(self, amount):
    #
    def calc_interest(self):
    #
    def get_balance(self):
        return self._balance

    def __str__(self):
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, self.account_id, self._balance, self.customer.last_name)


c1 = Customer("Anne","Smith","anne@smith.com")
a1 = Account(c1)
c2 = Customer("John", "Brown","john@brown.com")
print(c1)
print(a1)
print(c2)
