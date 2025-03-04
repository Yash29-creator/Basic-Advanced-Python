class Account:
    def __init__(self, acc_no, acc_name, balance):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.balance = balance
    def get_balance(self):
        print(f"Your current balance is {self.balance}")
    def get_bankDetails(self):
        print(f"Account Name: {self.acc_name}")
        print(f"Balance: {self.balance}")
    def withdraw(self, w):
        if w < self.balance:
            self.balance -= w
            print(f"Your current balance is {self.balance}")
        else:
            print(f"Insufficient Balance")
    def deposit(self, d):
        self.balance += d
        print(f"Your current balance is {self.balance}")

class Customer:
    def __init__(self, id, name):
        self.customerID = id
        self.customerName = name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def remove_account(self, account):
        self.accounts.remove(account)
    def total_accounts(self):
        print(f"Total number of accounts associated with {self.customerName} are {len(self.accounts)}")
    def get_accounts(self):
        return self.accounts

class Bank:
    def __init__(self, bankName, branch):
        self.bankName = bankName
        self.branch = branch
        self.customers = []
    def getBankName(self):
        print(f"Welcome to {self.branch} branch of {self.bankName}")
    def get_customers(self):
        return self.customers
    def add_customers(self, customer):
        self.customers.append(customer)
    def remove_customer(self, customer):
        self.customers.remove(customer)

acc_list = []
customer_list = []
bank_list = []

def bank_detail_func():
    input_bank = input("Enter bank name: ")
    b_list = []
    for i in bank_list:
        if i.bankName == input_bank:
            b_list.append(i)
    input_branch = input("Enter branch: ")
    br_list = []
    for i in b_list:
        if i.branch == input_branch:
            i.getBankName()
            for j in list(i.get_customers()):
                print(j)

def add_bank_func():
    bName = input("Enter Bank name: ")
    brName = input("Enter Branch name: ")
    bank_list.append(Bank(bName, brName))

def add_customer_bank_func(c_obj):
    which_bank = input("Which bank is customer associated with: ")
    f=0
    for i in bank_list:
        if i.bankName == which_bank:
            i.customers.append(c_obj)
            f=1
            break
    if f==0:
        print("Bank not found. Want to add bank: ")
        y_n=input("y or n: ")
        if y_n == 'y' or 'Y':
            brName = input("Enter Branch name: ")
            bank_list.append(Bank(which_bank, brName))
            for i in bank_list:
                if i.bankName == which_bank:
                    i.customers.append(c_obj)
                    break
        else:
            print("Deleting customer data...")
            customer_list.remove(c_obj)

def add_customer_func():
    c_id = input("Enter Customer ID: ")
    c_name = input("Enter Customer Name: ")
    c_obj = Customer(c_id,c_name)
    customer_list.append(c_obj)
    add_customer_bank_func(c_obj)


def add_acc_customer_func(a_obj):
    f = 0
    for i in customer_list:
        if i.customerName == a_obj.acc_name:
            i.accounts.append(a_obj)
            f = 1
            break
    if f == 0:
        print("Customer not found. Want to add Customer: ")
        y_n = input("y or n: ")
        if y_n == 'y' or 'Y':
            c_id = input("Enter Customer ID: ")
            c_name = a_obj.acc_name
            c_obj = Customer(c_id, c_name)
            customer_list.append(c_obj)
            add_customer_bank_func(c_obj)
            add_acc_customer_func(a_obj)
        else:
            print("Deleting account data...")
            acc_list.remove(a_obj)

def add_acc_func():
    acc_no_input = input("Enter Account Number: ")
    acc_name_input = input("Enter Account Name: ")
    acc_bal_input = float(input("Enter Account Balance: "))
    a_obj=Account(acc_no_input,acc_name_input,acc_bal_input)
    acc_list.append(a_obj)
    add_acc_customer_func(a_obj)

def acc_details_func():
    input_acc = input("Enter account number: ")
    for i in acc_list:
        if i.acc_no == input_acc:
            i.get_bankDetails()


def withdraw_func():
    input_acc = input("Enter account number: ")
    f=0
    for i in acc_list:
        if i.acc_no == input_acc:
            with_amnt = float(input("Enter Amount: "))
            i.withdraw(with_amnt)
            f = 1
    if f == 0:
        print("Account not found")


def deposit_func():
    input_acc = input("Enter account number: ")
    f = 0
    for i in acc_list:
        if i.acc_no == input_acc:
            deposit_amnt = float(input("Enter Amount: "))
            i.deposit(deposit_amnt)
            f = 1
    if f == 0:
        print("Account not found")


print("Enter any one choice for the service associated")
print("1.) Adding Bank\n2.) Bank Details.")
print("3.) Adding Customer.")
print("4.) Adding Account.\n5.) Account Details")
print("6.) Withdrawl.\n7.) Deposit")

while True:
    try:
        ch = int(input("Enter choice: "))
        if ch == 1:
            add_bank_func()
        elif ch == 2:
            bank_detail_func()
        elif ch == 3:
            add_customer_func()
        elif ch == 4:
            add_acc_func()
        elif ch == 5:
            acc_details_func()
        elif ch == 6:
            withdraw_func()
        elif ch == 7:
            deposit_func()
        else:
            break
    except ValueError:
        print("Please enter data properly")
    finally:
        print("Thank you for joining us! :)")