#!/bin/bash

# Kiểm tra xem script có quyền thực thi không
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or with sudo"
    exit
fi

# Bước 1: Cập nhật và nâng cấp các gói hệ thống
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Bước 2: Cài đặt Python và các phụ thuộc hệ thống
echo "Installing Python and required packages..."
sudo apt install -y python3 python3-pip python3-venv

# Bước 3: Cài đặt Git
echo "Installing Git..."
sudo apt install -y git

# Bước 4: Clone project từ GitHub (hoặc từ bất kỳ nơi nào bạn muốn)
echo "Cloning the repository..."
git clone https://github.com/TrinhDuongHoan/flask-tiny-app.git

# Bước 5: Di chuyển vào thư mục của project
cd flask-tiny-app || exit

# Bước 6: Tạo virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Bước 7: Kích hoạt virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Bước 8: Cài đặt các phụ thuộc từ requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Bước 9: Thiết lập cơ sở dữ liệu (nếu có migration)
echo "Running database migrations..."
python manage.py migrate

# Bước 10: Tạo superuser (optional, có thể bỏ qua)
echo "Creating superuser (you'll be prompted to enter username, email, and password)..."
python manage.py createsuperuser

# Bước 11: Khởi chạy server Django
echo "Starting Django development server..."
python manage.py runserver

# Thông báo hoàn tất
echo "Setup completed successfully!"
