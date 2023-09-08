# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy your Python script (app.py) into the container
COPY app.py .

# Install any dependencies your app may have (if any)
# RUN pip install package-name

# Specify the command to run when the container starts
CMD ["python", "app.py"]
