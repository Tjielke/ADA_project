import logging
import os

import connexion
from connexion.resolver import RestyResolver
from resources.sale import Bar_sale
from resources.product import Product
from resources.user import User
from db import Base, engine

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir="openapi/")
Base.metadata.create_all(engine)
app.add_api('delivery-service-api.yaml',
            arguments={'title': 'Deliver Service API'})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')