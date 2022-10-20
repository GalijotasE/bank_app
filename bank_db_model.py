from sqlalchemy import column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///bank.db')
Base = declarative_base()

class Person(Base):
    __tablename__ = "Users"
    id = column(Integer, primary_key = True)
    first_name = column("First Name", String)
    last_name = column("Last Name", String)
    personal_code = column("Personal Code", Integer)
    phone_number = column("Phone Number", String)

    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name}, {self.personal_code}, {self.phone_number}"

