# Pull the base image
FROM python:3.12.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY . /app

ENV DJANGO_SETTINGS_MODULE=social_book.settings
ENV PYTHONUNBUFFERED 1
COPY wait_for_db.py /wait_for_db.py
# Collect static files
RUN python manage.py collectstatic --noinput
EXPOSE 8000

# Run the application
CMD ["sh", "-c", "python /wait_for_db.py && python manage.py migrate && python create_superuser.py && gunicorn --bind 0.0.0.0:8000 --workers 3 social_book.wsgi:application"]
