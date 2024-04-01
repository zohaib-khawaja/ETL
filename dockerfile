# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Update and install dependencies
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 (or the port your app uses)
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "./main.py"]

# Copy README and other necessary files into the container
COPY README.md /path/in/container/README.md