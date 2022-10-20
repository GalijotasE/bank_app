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
    if action == "a":
        pass
    elif action == "v":
        pass
    elif action == "s":
        pass
    elif action == "q":
        break
    else:
        print("ERROR: Please only choose from given inputs!!!")


