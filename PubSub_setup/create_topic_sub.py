import logging

from pub_sub_util import create_subscription, create_topic

logging.getLogger().setLevel(logging.INFO)
create_topic("ada2024-413619", "bar_sale") # make sure to change the project id
create_subscription("ada2024-413619", "bar_sale", "inventory_check_sub")
create_subscription("ada2024-413619", "bar_sale", "balance_check_sub")
create_topic("ada2024-413619", "inventory_check_done") # make sure to change the project id
create_topic("ada2024-413619", "balance_check_done") # make sure to change the project id
create_subscription("ada2024-413619", "inventory_check_done", "bar_sale_service")
create_subscription("ada2024-413619", "balance_check_done", "bar_sale_service")