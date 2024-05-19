from datetime import datetime

from flask import jsonify

from constant import STATUS_CREATED
from daos.bar_sale_dao import Bar_sale_DAO
from daos.status_dao import StatusDAO
from daos.association import ProductInSale
from db import Session


class Bar_sale:
    @staticmethod
    def create(body):
        session = Session()
        sale = Bar_sale_DAO(body['buyer_id'], body['seller_id'],
                               datetime.strptime(body['sale_time'], '%Y-%m-%d %H:%M:%S.%f'),
                               StatusDAO(STATUS_CREATED, datetime.now()))
        print(sale.sale_time)
        session.add(sale)
        session.flush()  # Ensures 'sale' gets an ID before we use it in the association

        for product_info in body['product_ids']:  # Assuming product_ids is a list of dicts
            product_in_sale = ProductInSale(
                sale_id=sale.id,
                product_id=product_info['product_id'],
                quantity=product_info['quantity']
            )
            session.add(product_in_sale)
        
        
        
        
        # # Add products to the sale
        # for product_id in body.get('product_ids', []):
        #     product = session.query(Product_DAO).filter(Product_DAO.id == product_id).one()
        #     sale.sales.append(product)
            
            
        # session.add(sale)
        # session.flush()  # Ensures 'sale' gets an ID before we use it in the association

        # for product in body['product_ids']:
        #     print(product)
           
#            session.execute(product_in_sale.insert(), {
#                'sale_id': sale.id,
#                'product_id': product['product_id'],
#                'quantity': product['quantity']
#            })
#            sale.sales.append()
            
        session.add(sale)
        session.commit()
        session.refresh(sale)
        session.close()
        return jsonify({'sale_id': sale.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        sale = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == d_id).first()
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
        effected_rows = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == d_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no sale with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The sale was removed'}), 200
        
class Status:
    @staticmethod
    def update(d_id, status):
        session = Session()
        delivery = session.query(Bar_sale_DAO).filter(Bar_sale_DAO.id == d_id)[0]
        delivery.status.status = status
        delivery.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The sale status was updated'}), 200
