#!/bin/bash

cd ..

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Activating virtual environment..."
    source venv/bin/activate

    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt

    echo "Running database migrations..."
    python manage.py migrate

    read -p "Do you want to create a superuser? (y/n): " CREATE_SUPERUSER
    if [[ "$CREATE_SUPERUSER" == "y" || "$CREATE_SUPERUSER" == "Y" ]]; then
        echo "Creating superuser..."
        python manage.py createsuperuser
    fi

else
    echo "Virtual environment already exists."

    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo "Starting Django development server..."
python manage.py runserver

echo "Setup completed successfully!"
