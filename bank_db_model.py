from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///bank.db')
Base = declarative_base()

class Person(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    first_name = Column("First_Name", String)
    last_name = Column("Last_Name", String)
    personal_code = Column("Personal_Code", Integer)
    phone_number = Column("Phone_Number", String)
    accounts = relationship("Account", back_populates="Users")

    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name}, {self.personal_code}, {self.phone_number}"

class Account(Base):
    __tablename__ = "Accounts"
    id = Column(Integer, primary_key = True)
    account_number = Column("Account_Number", Integer)
    balance = Column("Balansas", Integer)
    person_id = Column("person_id", Integer, ForeignKey("Users.id"))
    person = relationship("Person", back_populates="accounts")
    bank_id = Column("Bank_id", Integer, ForeignKey("bank.id"))
    bank = relationship("Bank", back_populates ="Accounts")

    def __repr__(self):
        return f"({self.id}, {self.account_number}, {self.balance})"

