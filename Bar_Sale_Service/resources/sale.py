from datetime import datetime
from flask import jsonify
import json

from daos.bar_sale_dao import Bar_sale_DAO
from daos.product_dao import Product_DAO
from daos.association import ProductInSale
from daos.stock_dao import StockDAO
from daos.user_dao import UserDAO
from pub_sub_utils import publish_message
from db import Session


class Bar_sale:
    @staticmethod
    def create(body):
        session = Session()
        d_id = body['id']
        delivery = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == int(body['id'])).first()
        if delivery:
            session.close()
            return jsonify({'message': f'There is already delivery with id {d_id}'}), 403
        total_cost = 0
        for product in body['product_ids']:
            query_product = session.query(Product_DAO).filter(Product_DAO.id == int(product['product_id']))
            stock_product = session.query(StockDAO).filter(StockDAO.id == int(product['product_id'])).first()
            if int(stock_product.stock_position) >= product['quantity']:
                total_cost = total_cost + int(query_product['price'])*int(product['quantity'])
            else:
                session.close()
                return jsonify({'message': f'There is not enough stock to fulfill the order'}), 403
        balance_user = session.query(UserDAO).filter(UserDAO.id == int(body['buyer_id']))
        if balance_user['balance']<total_cost:
            session.close()
            return jsonify({'message': f'There is not enough balance in the account to fulfill the order'}), 403
        else: 
            sale = Bar_sale_DAO(body['id'],body['buyer_id'], body['seller_id'],datetime.now())
            session.add(sale)
            session.flush()  # Ensures 'sale' gets an ID before we use it in the association
            for product_info in body['product_ids']: 
                product_in_sale = ProductInSale(
                    id=product_info['id'],
                    sale_id=sale.id,
                    product_id=product_info['product_id'],
                    quantity=product_info['quantity']
                )
                session.add(product_in_sale)
                publish_message(project="adaprojects",topic="inventory_update",message=json.dumps({"id":product_info["product_id"], "amount_sold":product_info["quantity"]}).encode('utf-8'),event_type="Inventory")
            session.commit()
            session.refresh(sale)
            session.close()
        publish_message(project="adaprojects",topic="balance_update",message=json.dumps({"id":body["buyer_id"], "total_costs": 10}).encode('utf-8'),event_type="Balance")
        return jsonify({'sale_id': sale.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        sale = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == int(d_id)).first()
        print(sale.sale_time)
        if sale:
            status_obj = sale.status
            text_out = {
                "buyer_id:": sale.buyer_id,
                "seller_id": sale.buyer_id,
                "sale_time": sale.sale_time.isoformat(),
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no sale with id {d_id}'}), 404

    @staticmethod
    def delete(d_id):
        session = Session()
        effected_rows = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == int(d_id)).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no sale with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The sale was removed'}), 200
    
