# Use Python 3.10-slim as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . /app/

# Expose port 5000 and run the application
EXPOSE 5000
CMD ["python", "app.py"]
