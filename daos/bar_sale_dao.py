from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from daos.user_dao import UserDAO
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
    status = relationship(StatusDAO.__name__, backref=backref("delivery", uselist=False))
    buyer = relationship(UserDAO.__name__, backref=backref("delivery", uselist=False))
    seller = relationship(UserDAO.__name__, backref=backref("delivery", uselist=False))

    def __init__(self, buyer_id, seller_id, delivery_time, status,buyer,seller):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.delivery_time = delivery_time
        self.status = status
        self.buyer = buyer
        self.seller = seller
