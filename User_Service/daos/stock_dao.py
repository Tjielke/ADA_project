from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class StockDAO(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    stock_position = Column(String)
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self,id, stock_position, last_update):
        self.id = id
        self.stock_position = stock_position
        self.last_update = last_update
