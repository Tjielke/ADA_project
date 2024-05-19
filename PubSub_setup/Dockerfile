FROM python:3.10-slim
WORKDIR /app
COPY create_pubsub_resources.py /app/create_pubsub_resources.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "create_pubsub_resources.py"]
