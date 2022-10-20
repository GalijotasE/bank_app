#from bank_db_model import Person, Bank, Account, engine
from sqlalchemy.orm import sessionmaker
from bank_db_model import *

session = sessionmaker(bind=engine)

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
            print("---Add New User To The Database---")
            f_name = input("First Name: ")
            l_name = input("Last Name: ")
            p_code = input("Personal Code: ")
            p_number = input("Phone Number: ")
            


        elif action == "b":
            print("---Add New Bank To The Database---")
            pass
        elif action == "a":
            print("---Add New Account To The Database---")
            pass
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
            print("---List Of Users In The Database---")
            pass
        elif action == "b":
            print("---List Of Banks In The Database---")
            pass
        elif action == "a":
            print("---List Of Accounts In The Database---")
            pass
        elif action == "r":
            break
        else:
            print("ERROR: Please only choose from given inputs!!!")

##### Single user interface
    elif action == "s":
        print("---Single User Interface---")
        print("Please choose one of the given users:")

##### Quit
    elif action == "q":
        break
##### If input is incorrect
    else:
        print("ERROR: Please only choose from given inputs!!!")


