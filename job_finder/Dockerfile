# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run your Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
