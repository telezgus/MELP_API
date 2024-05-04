# Use a base Python image 
FROM python:3.11

# Install necessary packages
RUN apt-get update && \
    apt-get install -y binutils libproj-dev gdal-bin && \
    rm -rf /var/lib/apt/lists/*

# Copy application and necessary files
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
