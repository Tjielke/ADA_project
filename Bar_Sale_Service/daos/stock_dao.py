from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class StockDAO(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    stock = Column(String)
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, stock, last_update):
        self.stock = stock
        self.last_update = last_update
