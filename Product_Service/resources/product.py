from datetime import datetime

from flask import jsonify

from daos.bar_sale_dao import Bar_sale_DAO
from daos.product_dao import Product_DAO
from daos.association import ProductInSale
from daos.stock_dao import StockDAO
from daos.user_dao import UserDAO

from db import Session


class Product:
    @staticmethod
    def create(body):
        session = Session()
        product = Product_DAO(body['id'],body['name'], body['price'],
                               StockDAO(body['id'],0, datetime.now()))
        session.add(product)
        session.commit()
        session.refresh(product)
        session.close()
        return jsonify({'product_id': product.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        product = session.query(Product_DAO).filter(Product_DAO.id == int(d_id)).first()

        if product:
            stock_obj = product.stock
            text_out = {
                "name:": product.name,
                "price": product.price,
                "stock": {
                    "stock": stock_obj.stock,
                    "last_update": stock_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no product with id {d_id}'}), 404

    @staticmethod
    def delete(d_id):
        session = Session()
        effected_rows = session.query(Product_DAO).filter(Product_DAO.id == int(d_id)).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no product with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The product was removed'}), 200
        