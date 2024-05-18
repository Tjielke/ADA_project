from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.bar_sale_dao import Bar_sale_DAO
from daos.product_dao import Product_DAO

from db import Base


class Product_in_sale_DAO(Base):
    __tablename__ = 'insale'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    # reference to product as foreign key relationship. This will be automatically assigned.
    sale_id = Column(Integer, ForeignKey('sale.id'))
    # reference to bar sale as foreign key relationship. This will be automatically assigned.
    product_id = Column(Integer, ForeignKey('product.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    sale = relationship(Bar_sale_DAO.__name__, backref=backref("insale", uselist=False))
    product = relationship(Product_DAO.__name__, backref=backref("insale", uselist=False))

    def __init__(self, sale_id, product_id, sale, product):
        self.sale_id = sale_id
        self.product_id = product_id
        self.sale = sale
        self.product = product
