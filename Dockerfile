# Use the official Python base image
FROM python:3.14-slim

# Set the working directory
#WORKDIR files
# Copy the requirements.txt file into the container
COPY files/config.json ./
COPY files/main.py ./
COPY requirements.txt ./

ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Start the Discord bot
CMD ["python", "main.py"]