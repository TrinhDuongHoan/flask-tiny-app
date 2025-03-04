@echo off

REM
cd ..

REM
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv

    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt

    echo Running database migrations...
    python manage.py migrate

    echo Creating superuser...
    python manage.py createsuperuser
) else (
    echo Virtual environment already exists.
    echo Activating virtual environment...
    call venv\Scripts\activate
)

REM
echo Starting Django development server...
python manage.py runserver

REM
echo Setup completed successfully!
pause
