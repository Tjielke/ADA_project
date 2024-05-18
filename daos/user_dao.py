from sqlalchemy import Column, String, Integer, DateTime, ForeignKey,Float
from sqlalchemy.orm import relationship, backref

from db import Base


class UserDAO(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    name = Column(String)
    balance = Column(Float)
    date_of_birth = Column(DateTime)

    def __init__(self, name, balance, date_of_birth):
        self.name = name
        self.balance = balance
        self.date_of_birth = date_of_birth

