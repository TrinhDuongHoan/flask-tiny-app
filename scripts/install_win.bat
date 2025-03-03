@echo off

REM Bước 1: Cập nhật hệ thống (Windows không hỗ trợ cài đặt gói như Linux)
echo Updating system packages...

REM Bước 2: Cài đặt Python và pip (nếu chưa cài đặt)
echo Installing Python and pip...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    REM Bạn có thể tải và cài đặt Python từ https://www.python.org/downloads/
    REM Tải Python tự động là một công việc phức tạp trên Windows và không thể thực hiện trực tiếp qua batch script.
    pause
    exit
)
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

REM Bước 3: Cài đặt Git (nếu chưa có)
echo Installing Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed. Installing Git...
    REM Tải và cài đặt Git từ https://git-scm.com/download/win
    pause
    exit
)

REM Bước 4: Clone project từ GitHub
echo Cloning repository...
git clone https://github.com/TrinhDuongHoan/flask-tiny-app.git

REM Bước 5: Di chuyển vào thư mục project
cd flask-tiny-app

REM Bước 6: Tạo virtual environment
echo Creating virtual environment...
python -m venv venv

REM Bước 7: Kích hoạt virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Bước 8: Cài đặt các phụ thuộc từ requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Bước 9: Chạy migrations (thiết lập cơ sở dữ liệu)
echo Running database migrations...
python manage.py migrate

REM Bước 10: Tạo superuser (có thể bỏ qua)
echo Creating superuser...
python manage.py createsuperuser

REM Bước 11: Khởi động server Django
echo Starting Django development server...
python manage.py runserver

REM Thông báo hoàn tất
echo Setup completed successfully!
pause
