from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class StockDAO(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    stock = Column(String)
    create_date = Column(TIMESTAMP(timezone=False))
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self,id, stock,create_date, last_update):
        self.id = id
        self.stock = stock
        self.create_date = create_date
        self.last_update = last_update
