# Use an official Python image as a base image
FROM python:3.9-slim

# Install dependencies for Chromium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libx11-xcb1 \
    libnspr4 \
    libnss3 \
    libxss1 \
    xdg-utils \
    chromium

# Set up the working directory
WORKDIR /app

# Copy your script into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install chromedriver-autoinstaller
RUN pip install chromedriver-autoinstaller

# Run the script
CMD ["python", "app.py"]
