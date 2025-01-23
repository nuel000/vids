# Use the official Playwright image as the base image
FROM mcr.microsoft.com/playwright:focal

# Set the working directory
WORKDIR /app

# Copy the script and requirements file
COPY . .

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install beautifulsoup4

# Run the script
CMD ["python3", "app.py"]
