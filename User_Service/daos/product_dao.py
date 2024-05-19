from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.stock_dao import StockDAO
from daos.association import ProductInSale
from db import Base


class Product_DAO(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    name = Column(String)
    price = Column(String)
    # reference to status as foreign key relationship. This will be automatically assigned.
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = relationship(StockDAO.__name__, backref=backref("product", uselist=False))
    products = relationship(ProductInSale.__name__, back_populates="product")

    def __init__(self,id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
