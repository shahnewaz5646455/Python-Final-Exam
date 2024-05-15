import random
class Bank:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.balance=1000
        self.loan=0
        self.loan_feature=True
Admin_Account={}
class Admin:
    def __init__(self,name,email,password):
        self.password=password
        self.name=name
        self.email=email
        Admin_Account[self.email]=self
    def delete_account(self,account_num):
        if account_num in Account.keys():
            del Account[account_num]
            print("....DELETE SUCCESSFULL....")
        else:
            print("ACCOUNT NOT EXIST ")

        
    def show_account(self):
        for key,value in Account.items():
            print(f"Account Number:{key} Name :{value.name} Balance :{value.balance}TK")
    def bank_balance(self,bank):
        print(f"Total Balance Of BANK IS : {bank.balance}TK")
    def total_loan(self,bank):
        print(f"Total amount of LOAN IS : {bank.loan}TK")   
    def loan_feature(self,on_off,bank):
        if on_off==1:
            bank.loan_feature=True
            print("........LOAN FEATURE IS << ON >>.........")
        elif on_off==0:
            bank.loan_feature=False
            print("........LOAN FEATURE IS << OFF >>.........")
        else:
            print("INVALID INPUT")



Account={}  

class BankAccount:
    def __init__(self, name, email, address, account_type,password):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.password=password
        self.account_number = random.randint(100000, 999999)
        Account[self.account_number]=self
        self.history={}
        self.loan_count=0
    

    def deposit(self, amount,bank):
        Account[self.account_number].balance += amount
        self.transaction_id=random.randint(888, 999999)
        self.history[self.transaction_id]=f"deposit {amount}"
        bank.balance+=amount
        print(f"Your Balance IS : {Account[self.account_number].balance} TK")

    def withdraw(self, amount,bank):
        if bank.balance<amount:
            print("BANK is bankrupt")
        else:
            if amount > self.balance:
                print("Withdrawal amount exceeded")
            else:
                Account[self.account_number].balance -= amount
                self.transaction_id=111+random.randint(888, 999999)
                self.history[self.transaction_id]=f"withdraw {amount}"
                bank.balance-=amount
        
        print("Current balance IS: ",Account[self.account_number].balance,"TK")

    def check_balance(self):
        return f"....YOUR BALANCE IS : {Account[self.account_number].balance}TK..."
    def loan(self,amount,bank):
        if bank.loan_feature==True:
            if bank.balance<amount:
                print("BANK is bankrupt")
            else:
                if Account[self.account_number].loan_count<2:
                    print("....LOAN FEATURE IS ...**ON**...")
                    Account[self.account_number].balance += amount
                    Account[self.account_number].loan_count+=1
                    bank.loan+=amount
                    bank.balance-=amount
                    print("Current balance IS: ",Account[self.account_number].balance,"TK")

                else:
                    print("You have alrady took loan two times")

            
        else:
            print("LOAN FEATURE IS ...OFF...")
            


    def Account_balance(self,account_num):
        return Account[account_num].balance
    
    def Money_transfer(self,amount,recever_account):
        
        self.c=0
        for key,value in Account.items():
            
            if key==recever_account:
                self.c=1
        if self.c==1: 

            if amount > Account[self.account_number].balance:
                    print("No sufficient BALANCE")
            else:
                Account[self.account_number].balance -= amount
                Account[recever_account].balance+=amount
                self.transaction_id=222+random.randint(888, 999999)
                self.history[self.transaction_id]=f"transfer to {recever_account} :  {amount}TK"
                print("Transfer successfull")
                print(" Current balance:",Account[self.account_number].balance,"TK")

            
        else:
            print("Account does not exist")

    
    def T_history(self):
        for key,value in self.history.items():
            print(f"transaction_id : {key}  {value}")
                
    


bank=Bank("City Bank","Mirpur")



account1 = BankAccount('Doe', 'johndoe@example.com', '123 Street, City', 'Savings',123324)
account2 = BankAccount('nii Doe', 'johndoe@example.com', '123 Street, City', 'Savings',248739)



def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    account_type = input("Account Type : ")
    password = input("Password : ")
    account= BankAccount(name=name,email=email,address=address,account_type=account_type,password=password)


    while True:
        print(f".............Welcome {account.name}!!..........")
        print(f"Your Account Number is : {account.account_number}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. check available balance")
        print("4. check transaction history")
        print("5. transfer money")
        print("6. LOAN")
        print("7. EXIT")


        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            amount=int(input("Amount : "))
            account.deposit(amount=amount,bank=bank)
            
        elif choice == 2:
            amount=int(input("Amount : "))
            account.withdraw(amount=amount,bank=bank)
            
        elif choice == 3:
            print(account.check_balance())
            
        elif choice == 4:
            account.T_history()

        elif choice == 5:
            amount=int(input("Amount : "))
            recever_account=int(input("Recever_account: "))
            account.Money_transfer(amount=amount,recever_account=recever_account)
        elif choice == 6:
            amount=int(input("Amount : "))
            account.loan(amount,bank)
        elif choice == 7:
            break
        else:
            print("Invalid Input")





def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    password = input("Enter Your Password: ")
    admin = Admin(name=name, email=email,password=password)
    
    
    while True:
        
        print(f"Welcome {admin.name}!!")
        print("1. Delete Account")
        print("2. Show Account")
        print("3. Bank Balance")
        print("4. Loan Amount")
        print("5. Loan Feature")
        print("6. Exit\n")

        choice = int(input("Enter Your Choice : "))
        print("\n")
        if choice == 1:
            Account_number=int(input("Account number: "))
            admin.delete_account(account_num=Account_number)
            
            
        elif choice == 2:
            admin.show_account()
        elif choice == 3:
            admin.bank_balance(bank)
        elif choice == 4:
            admin.total_loan(bank)
        elif choice == 5:
            on_off=int(input("Write 1 to ON or 0 to OFF  :"))
            admin.loan_feature(on_off,bank)
        elif choice == 6:
            break
        else:
            print("Invalide Input")

def alrady_admin():
    email = input("Enter Your Email : ")
    password = input("Enter Your Password: ")
    c=0
    for key,value in Admin_Account.items():
        if key==email and value.password==password:
            c=1
    if c==1:
        while True:
        
            print(f"Welcome {Admin_Account[email].name}!!")
            print("1. Delete Account")
            print("2. Show Account")
            print("3. Bank Balance")
            print("4. Loan Amount")
            print("5. Loan Feature")
            print("6. Exit\n")

            choice = int(input("Enter Your Choice : "))
            print("\n")
            if choice == 1:
                Account_number=int(input("Account number: "))
                Admin_Account[email].delete_account(account_num=Account_number)
                
                
            elif choice == 2:
                Admin_Account[email].show_account()
            elif choice == 3:
                Admin_Account[email].bank_balance(bank)
            elif choice == 4:
                Admin_Account[email].total_loan(bank)
            elif choice == 5:
                on_off=int(input("Write 1 to ON or 0 to OFF  :"))
                Admin_Account[email].loan_feature(on_off,bank)
            elif choice == 6:
                break
            else:
                print("Invalide Input")
    else:
        print("Invalid Information")


def Login():
    account_num = int(input("Account Number:  "))
    password= int(input("Password:  "))
    f=0
    for key,value in Account.items():
        if account_num==key and value.password==password:
            f=1
            
    if f==1:
        while True:
            print(f".............Welcome {Account[account_num].name}!!...........")
            print(f"Your Account Number is : {Account[account_num].account_number}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. check available balance")
            print("4. check transaction history")
            print("5. transfer money")
            print("6. LOAN")
            print("7. EXIT\n")
            choice = int(input("Enter Your Choice : "))
            print("\n")
            if choice == 1:
                amount=int(input("Amount : "))
                Account[account_num].deposit(amount=amount,bank=bank)
                
            elif choice == 2:
                amount=int(input("Amount : "))
                Account[account_num].withdraw(amount=amount,bank=bank)
                
            elif choice == 3:
                print(Account[account_num].check_balance())
                
            elif choice == 4:
                Account[account_num].T_history()

            elif choice == 5:
                amount=int(input("Amount : "))
                recever_account=int(input("Recever_account: "))
                Account[account_num].Money_transfer(amount=amount,recever_account=recever_account)
            elif choice == 6:
                amount=int(input("Amount : "))
                Account[account_num].loan(amount,bank)
            elif choice == 7:
                break
            else:
                print("Invalid Input")
    elif f==0:
        print("Account NOT exist")
    else:
        print("INVALID INPUT")

cnt=0
while True:
    print("...........Welcome TO BANK......!!")
    print("1. Alredy Have An Account")
    print("2. NEW Customer")
    print("3. Admin")
    print("4. Exit\n")
    choice = int(input("Enter your choice : "))
    print("\n")
    
    if choice==1:
        Login()

    elif choice == 2:
        customer_menu()
    elif choice == 3:
        if cnt==0:
            admin_menu()

        else:
            alrady_admin()
        cnt+=1

        
    elif choice == 4:
        break
    else:
        print("Invalid Input!!")






