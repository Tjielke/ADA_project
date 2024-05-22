Before you run, a few steps to take in order to maker everything work:
You will need to update the project-id in multiple files, the current project used is 'adaprojects' so you can change this to your own project id using ctr+f in the files listed below:
Bar_Sale_Service/recourses/sale.py
Bar_Sale_Service/db.py
Bar_Sale_Service/Dockerfile
Bar_Sale_Service/bar_sale_service.py
Product_Service/db.py
Product_Service/Dockerfile
User_Service/db.py
User_Service/Dockerfile

Next up you will have to create the BigQuery DataBase. Create this database within the same project as just entered and call the database bardb.

Next up we can create a vm and clone the git repository, after cloning run 'sudo docker-compose up -d' to start the services and create the topics

Next step is to create the FaaS functions in your own Google Cloud Workflows, you will need to create two functions:
'update-balance' add pub/sub trigger with 'balance_update' as topic name, and go to FaaS_Functions/update-balance.yaml to find the yaml code for the workflow.
'update-invetory' add pub/sub trigger with 'inventory_update' as topic name, and go to FaaS_Functions/update-inventory.yaml to find the yaml code for the workflow.

When adding a new sale by using the Insomnia API call with the correct keycloak configuration, the Google Workflow should now be called when the sale is accepted.




# Project Setup Guide

Before running the project, follow these steps to ensure everything works smoothly:

## Update Project ID

You will need to update the `project-id` in multiple files. The current project ID used is `adaprojects`. Change this to your own project ID by using `Ctrl+F` in the following files:

- `Bar_Sale_Service/resources/sale.py`
- `Bar_Sale_Service/db.py`
- `Bar_Sale_Service/Dockerfile`
- `Bar_Sale_Service/bar_sale_service.py`
- `Product_Service/db.py`
- `Product_Service/Dockerfile`
- `User_Service/db.py`
- `User_Service/Dockerfile`

## Create BigQuery Database

Create the BigQuery database within the same project you just configured. Name the database `bardb`.

## Set Up VM and Services

1. Create a virtual machine (VM).
2. Clone the Git repository to the VM.
3. Run the following command to start the services and create the topics:
   ```bash
   sudo docker-compose up -d

## Create Google Cloud Workflows Functions

Create the following FaaS functions in your Google Cloud Workflows:

1. **`update-balance`**
    - Add a Pub/Sub trigger with `balance_update` as the topic name.
    - Refer to `FaaS_Functions/update-balance.yaml` for the YAML code for this workflow.

2. **`update-inventory`**
    - Add a Pub/Sub trigger with `inventory_update` as the topic name.
    - Refer to `FaaS_Functions/update-inventory.yaml` for the YAML code for this workflow.

## Adding a New Sale

When adding a new sale using the Insomnia API call with the correct Keycloak configuration, the Google Workflow should be triggered when the sale is accepted.

