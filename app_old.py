import json
import logging
import os
from google.cloud import storage

import pandas as pd
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/User/create', methods=['POST'])
def create_user():
    # retrieving project information
    project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
    user_repo = os.environ.get('USER_REPO', 'Specified environment variable is not set.')
    
    user_data = request.get_json()
    df = pd.read_json(json.dumps(user_data), orient='records')
    
    # Save DataFrame to a CSV file
    file_path = os.path.join('/tmp', 'data.csv')
    df.to_csv(file_path, index=False)
    # Save to GCS
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(user_repo)
    blob = bucket.blob("user_1")
    blob.upload_from_filename(file_path)
    
    # Do clean up
    os.remove(file_path)

    # Saving model in a given location provided as an env. variable
    return 200


app.run(host='0.0.0.0', port=5000)
