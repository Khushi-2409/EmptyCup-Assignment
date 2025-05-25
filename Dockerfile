# Use Python as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend/ /app/backend

# Copy frontend (optional: if you plan to serve it through the backend)
COPY frontend/ /app/frontend

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run Flask app
CMD ["flask", "run"]
