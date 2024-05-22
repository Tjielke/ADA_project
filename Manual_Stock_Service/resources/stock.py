from datetime import datetime

from flask import jsonify
from daos.bar_sale_dao import Bar_sale_DAO
from daos.stock_dao import StockDAO
from daos.product_dao import Product_DAO
from db import Session


class Stock:
    @staticmethod
    def update(d_id, new_stock):
        session = Session()
        Stock = session.query(StockDAO).filter(StockDAO.id == int(d_id))[0]
        Stock.id = d_id
        Stock.stock = str(new_stock['stock'])
        Stock.create_date = datetime.now()
        Stock.last_update = datetime.now()
        session.commit()
        return jsonify({'message': 'The stock position was updated'}), 200
