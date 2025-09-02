# Use a lightweight Python image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Upgrade pip first
RUN python -m pip install --upgrade pip

# Copy requirements.txt first (to leverage Docker cache)
COPY requirements.txt .

# Install Python dependencies (ensure latest xgboost)
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --upgrade xgboost

# Copy all your app files into the container
COPY . .

# Default command (can be overridden by docker run)
CMD ["python", "data_ingest.py"]
