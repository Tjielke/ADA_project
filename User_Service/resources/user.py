from datetime import datetime

from flask import jsonify

from daos.bar_sale_dao import Bar_sale_DAO
from daos.product_dao import Product_DAO
from daos.stock_dao import StockDAO
from daos.association import ProductInSale
from daos.user_dao import UserDAO
from db import Session


class User:
    @staticmethod
    def create(body):
        session = Session()
        user = UserDAO(body['id'],body['name'], body['balance'],
                       datetime.strptime(body['date_of_birth'], '%Y-%m-%d').date()
                       )
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return jsonify({'user_id': user.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        user = session.query(UserDAO).filter(UserDAO.id == int(d_id)).first()

        if user:
            text_out = {
                "name:": user.name,
                "balance": user.balance,
                "date_of_birth": user.date_of_birth,
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no user with id {d_id}'}), 404

    @staticmethod
    def delete(d_id):
        session = Session()
        effected_rows = session.query(UserDAO).filter(UserDAO.id == int(d_id)).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no user with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The user was removed'}), 200
    
