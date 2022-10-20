from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///bank.db')
Base = declarative_base()

class Person(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    personal_code = Column("personal_code", Integer, unique = True)
    phone_number = Column("phone_number", String)
    accounts = relationship("Account", back_populates="user")

    def __init__(self, first_name, last_name, personal_code, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_code = personal_code
        self.phone_number = phone_number

    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name}, {self.personal_code}, {self.phone_number}"

class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key = True)
    name = Column("bank_name", String)
    address = Column("address", String)
    swift = Column("swift", String)
    accounts = relationship("Account", back_populates = "banks")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.address}, {self.swift}, {self.accounts})"

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key = True)
    account_number = Column("account_number", Integer)
    balance = Column("balansas", Float)
    bank_id = Column("bank_id", Integer, ForeignKey("bank.id"))
    user_id = Column("user_id", Integer, ForeignKey("user.id"))
    user = relationship("Person", back_populates = "accounts")
    banks = relationship("Bank", back_populates = "accounts")

    def __repr__(self):
        return f"({self.id}, {self.account_number}, {self.balance})"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

