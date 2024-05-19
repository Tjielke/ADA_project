from sqlalchemy import Column, String, Integer, Date,Float

from db import Base


class UserDAO(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    name = Column(String)
    balance = Column(Float)
    date_of_birth = Column(Date)

    def __init__(self,id, name, balance, date_of_birth):
        self.id = id
        self.name = name
        self.balance = balance
        self.date_of_birth = date_of_birth

