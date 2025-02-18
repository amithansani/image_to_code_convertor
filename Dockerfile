# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install libgomp1
RUN apt-get update && apt-get install -y \
    libgomp1 \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Define environment variable
ENV NAME=imgtocd

# Run the command to start the development server
CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000"]