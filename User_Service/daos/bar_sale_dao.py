from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

#from daos.association import product_in_sale
from daos.status_dao import StatusDAO
from daos.user_dao import UserDAO
from daos.association import ProductInSale
from db import Base


class Bar_sale_DAO(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    buyer_id = Column(Integer, ForeignKey('user.id'))
    seller_id = Column(Integer, ForeignKey('user.id'))
    sale_time = Column(DateTime)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("sale", uselist=False))
    buyer = relationship(UserDAO.__name__,foreign_keys=[buyer_id], backref=backref("purchase", uselist=False))
    seller = relationship(UserDAO.__name__,foreign_keys=[seller_id], backref=backref("sales", uselist=False))
    sales = relationship(ProductInSale.__name__, back_populates="sale")
    
    def __init__(self,id, buyer_id, seller_id, sale_time, status):
        self.id = id
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.sale_time = sale_time
        self.status = status
