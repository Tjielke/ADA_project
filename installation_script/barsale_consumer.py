import logging
import time
import schedule

from google.cloud import pubsub_v1





def pull_message(project, subscription):
    subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=project,
        sub=subscription
    )
    logging.info(f"Reading data from created: {subscription_name}")
    with pubsub_v1.SubscriberClient() as subscriber:
        future = subscriber.subscribe(subscription_name, callback)
        try:
            future.result()
        except Exception as ex:
            logging.info(ex)
            logging.info(f"Listening for messages on {subscription_name} threw an exception: {ex}.")
            time.sleep(30)


def callback(message):
    logging.info(f"Received {message}.")
    message.ack()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    schedule.every().minute.at(':00').do(pull_message, "your_project_id", "order_status_user_sub")
    while True:
        schedule.run_pending()
        time.sleep(.1)
