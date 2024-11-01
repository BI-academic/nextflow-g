# Use a Python 3.10 Alpine image as a base
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /code

# Environment variables for Flask
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=production

# Install necessary packages for SQLite3 and building dependencies
RUN apk add --no-cache gcc musl-dev linux-headers sqlite

# Copy the requirements file and install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Copy the source code into the container
COPY src/ /code

# Initialize the SQLite3 database using the SQL file
RUN sqlite3 /code/nextflow_g.db < /code/db/initial.sql

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]