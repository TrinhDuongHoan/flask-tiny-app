FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y python3-distutils python3-setuptools python3-pip

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate || echo "Migration failed, continuing..."

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]