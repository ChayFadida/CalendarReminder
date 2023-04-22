FROM python:3.10

# set work directory
WORKDIR /CalanderReminder

# set environment variables
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container
COPY requirement.txt .

# Install any needed packages specified in requirements.txt
RUN apt-get update 
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirement.txt

# Copy the current directory contents into the container at /app
COPY . /CalanderReminder

# Expose port 8000 for the Django app
EXPOSE 8000