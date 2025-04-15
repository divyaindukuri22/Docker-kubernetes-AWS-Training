# Use Python image as base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app code
COPY app/ .

# Expose port
EXPOSE 8080

# Start the Flask app
CMD ["python", "app.py"]
