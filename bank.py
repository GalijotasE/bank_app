from bank_db_model import Person, Bank, Account, engine
from sqlalchemy.orm import sessionmaker
from bank_db_model import *

Session = sessionmaker(bind=engine)
session = Session()

### show all users in the database.
def show_all_users():
    print("---List Of Users In The Database---")
    users = session.query(Person).all()
    for user in users:
        print(user)

### show all banks in the database.
def show_all_banks():
    print("---List Of Banks In The Database---")
    banks = session.query(Bank).all()
    for bank in banks:
        print(bank)

### show all accounts in the database.
def show_all_accounts():
    print("---List Of Accounts In The Database---")
    accounts = session.query(Account).all()
    for account in accounts:
        print(account)

### add new user to the database.
def insert_new_user():
    print("---Add New User To The Database---")
    try:
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        p_code = input("Personal Code: ")
        p_number = input("Phone Number: ")
    except ValueError:
        print("ERROR!!")
        return
    else:
        new_user = Person(
            first_name=f_name,
            last_name=l_name,
            personal_code=p_code,
            phone_number=p_number
        )
        session.add(new_user)
        session.commit()
        print(f"User {f_name} was successfully added to the database.")

### add new bank to the database.
def insert_new_bank():
    print("---Add New Bank To The Database---")
    try:
        b_name = input("Name Of The Bank: ")
        b_address = input("Address Of The Bank: ")
        b_swift = input("Swift Code Of The Bank: ")
    except ValueError:
        print("ERROR!!")
        return
    else:
        new_bank = Bank(
            name= b_name,
            address= b_address,
            swift= b_swift
        )
        session.add(new_bank)
        session.commit()
        print(f"Bank {b_name} was successfully added to the database.")

### add new account to database.
def insert_new_account():
    print("---Add New Account To The Database---")
    try:
        n_account = input("Account Number: ")
        n_balance = input("Account Balance: ")
        print("Choose the user id: ")
        show_all_users()
        n_user_id = input("User id: ")
        print("Choose the bank id: ")
        show_all_banks()
        n_bank_id = input("Bank id: ")
    except ValueError:
        print("ERROR!!")
    else:
        new_account = Account(
            account_number=n_account,
            balance= n_balance,
            user_id= n_user_id,
            bank_id= n_bank_id
        )
        session.add(new_account)
        session.commit()
        print(f"Bank {n_account} was successfully added to the database.")

while True:
    print("---Bank Application---")
    print("Please choose one of the following:")
    print("a - Add new data to the database") # leistu ivesti asmenis, bankus, saskaitas.
    print("v - View all data from the database") # leistu perziureti asmenis, bankus, saskaitas.
    print("s - Single user interface") # leistu perziureti pasirinkto asmens varda, pavarde, balansa, banko koda, saskaitos numeri, leistu daryti pavedima.
    print("q - Quit")
    action = input("Please choose: ").casefold()

##### Add new data to the database
    if action == "a":
        print("---Adding Data To The Database---")
        print("Please choose one of the following:")
        print("u - Insert new user to the database")
        print("b - Insert new bank to the database")
        print("a - insert new account to the database")
        print("r - Return to a menu screen")
        action = input("Please choose: ").casefold()
        # Add new user to the database
        if action =="u":
            insert_new_user()
        elif action == "b":
            insert_new_bank()
        elif action == "a":
            insert_new_account()
        elif action =="q":
            break
        else:
            print("ERROR: Please only choose from given inputs!!!")

##### View all data from the database
    elif action == "v":
        print("---View Data From The Database---")
        print("Please choose one of the following:")
        print("u - View all user data from the database")
        print("b - View all banks data from the database")
        print("a - View all accounts data from the database")
        print("r - Return to a menu screen:")
        action = input("Please choose: ").casefold()
        if action =="u":
            show_all_users()
        elif action == "b":
            show_all_banks()
        elif action == "a":
            show_all_accounts()
        elif action == "r":
            print("The applications is closing...")
            print("Thank you for using this app.")
            break
        else:
            print("ERROR: Please only choose from given inputs!!!")

##### Single user interface
    #elif action == "s":
        #print("---Single User Interface---")
        #print("Please choose one of the given users:")
        #show_all_users()

##### Quit
    elif action == "q":
        break
##### If input is incorrect
    else:
        print("ERROR: Please only choose from given inputs!!!")


