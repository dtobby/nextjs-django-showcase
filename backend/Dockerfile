# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents python from writing .pyc files
ENV PYTHONUNBUFFERED 1         # Prevents python from buffering stdout/stderr

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any - good practice to update)
# We might need build-essential or other libs later for some packages,
# but psycopg2-binary often avoids this need for basic postgres.
# RUN apt-get update && apt-get install -y --no-install-recommends some-package

# Install Python dependencies
# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the Django app runs on (default is 8000)
EXPOSE 8000

# Define the command to run your app using Gunicorn (a production-ready server)
# We'll install gunicorn via requirements.txt later when needed for production.
# For now, we can use the Django development server, but we'll set up
# the docker-compose to override this command during development.
# CMD ["gunicorn", "productBackendCore.wsgi:application", "--bind", "0.0.0.0:8000"]
# Default command for development (will be overridden by docker-compose):
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]