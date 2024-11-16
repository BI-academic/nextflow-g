# Use a Python 3.10 Alpine image as a base
FROM nextflow/nextflow:24.04.4

# Installing essential packages
RUN yum update -y && yum install -y wget

# Make default Python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1

# Download pip and install
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Set the working directory inside the container
WORKDIR /code

# Environment variables for Flask
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=production

# Copy the requirements file and install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Copy the source code into the container
COPY src/ /code

# Initialize the SQLite3 database using the SQL file
# RUN sqlite3 /code/db/nextflow_g.db < /code/db/initial.sql

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]