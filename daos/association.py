from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class ProductInSale(Base):
    __tablename__ = 'product_in_sale'
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey('sale.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False, default=1)

    sale = relationship("Bar_sale_DAO", back_populates="sales")
    product = relationship("Product_DAO", back_populates="products")