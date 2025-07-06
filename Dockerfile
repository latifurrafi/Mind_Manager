#Base image
FROM python:3.11-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set Work DIrectory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Project Files
COPY . /code/

# Expose port (adjust if needed)
EXPOSE 8080

# Default Command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

