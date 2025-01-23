# Use an official Python image as a base image
FROM python:3.9-slim

# Install dependencies for Chrome and ChromeDriver
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
    gnupg2 \
    lsb-release \
    sudo

# Add Google's official Chrome repository and install Chrome
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | tee /etc/apt/trusted.gpg.d/google.asc && \
    DISTRO=$(lsb_release -c | awk '{print $2}') && \
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/google.asc] https://dl.google.com/linux/chrome/deb/ $DISTRO main" | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver (matching version with installed Chrome)
RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{print $3}') && \
    wget https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Set up the working directory
WORKDIR /app

# Copy your script into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "app.py"]
