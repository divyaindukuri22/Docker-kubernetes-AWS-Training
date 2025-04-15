# Use an official Python runtime
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

