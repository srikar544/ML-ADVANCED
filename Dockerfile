# Use a lightweight Python image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Upgrade pip, setuptools, and wheel for smooth installs
RUN python -m pip install --upgrade pip setuptools wheel

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Default command (can be overridden by docker run)
# You can change this to train.py, data_ingest.py, or feature_engineer.py as needed
CMD ["python", "train.py"]
