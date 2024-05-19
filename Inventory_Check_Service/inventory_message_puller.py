import json
import logging
import time
from threading import Thread

import schedule
from google.cloud import pubsub_v1
from pub_sub_util import publish_message

from daos.product_dao import Product_DAO
from daos.stock_dao import StockDAO
from daos.bar_sale_dao import Bar_sale_DAO
from db import Session


def check(order_details):
    session = Session()
    try:
        for item in order_details:
            product_id = item['product_id']
            required_quantity = item['quantity']

            product = session.query(Product_DAO).filter(Product_DAO.id == int(product_id)).first()
            if not product or product.stock.stock < required_quantity:
                return False, f"Not enough stock for product {product_id}"

        return True, "Stock is sufficient"
    finally:
        session.close()


def pull_message(project, subscription, orders):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project, subscription)

    def callback(self, message):
        logging.info(f"Received {message.data}.")
        event_type = message.attributes.get("event_type")  # event type as a message attribute
        data = json.loads(message.data.decode("utf-8"))
        inventory = check(data["order_details"])
        if inventory:
            data = {
                "message": "The requested quantity can be satisfied"
            }
            data = json.dumps(data).encode("utf-8")
            publish_message(project=self.project, topic="inventory_check_done", message=data,
                            event_type="CheckDone")
        else:
            data = {
                "message": "The requested quantity cannot be satisfied"
            }
            data = json.dumps(data).encode("utf-8")
            publish_message(project=self.project, topic="inventory_check_done", message=data,
                            event_type="CheckFailed")

    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=callback, await_callbacks_on_shutdown=True,
    )
    logging.info(f"Listening for messages on {subscription_path}..\n")
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=60.0)
        except Exception as ex:
            logging.info(ex)
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.


class MessagePuller:
    def __init__(self, project, subscription, orders):
        self.project_id = project
        self.subscription_id = subscription
        self.orders = orders

    def run(self):
        schedule.every().minute.at(':00').do(pull_message, self.project_id, self.subscription_id, self.orders)
        while True:
            try:
                schedule.run_pending()
                time.sleep(.1)
            except Exception as ex:
                logging.info(ex)
