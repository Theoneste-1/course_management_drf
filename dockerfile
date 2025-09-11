FROM python:3.11-slim-bullseye

# Set environment variables

# Prevents Python from writing .pyc files, reducing image size.
ENV PYTHONDONTWRITEBYTECODE=1

# Ensurej b,. e6 shj./ jp vm-g fcgu-0 67U,YN 45ps Python output is sent directly to container logs.
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy thei requirements file and isntall dependencies
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the database migrations (optional but often needed for apis)
RUN python manage.py migrate

# Expoose the port you DJANGO APP WILL run on
EXPOSE 8000

# Command to run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Command to run the Django for application with Gunocorn(for production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "course_manage.wsgi:application"]
