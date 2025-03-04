# Flask Tiny App
## Thông tin sinh viên :
- Trịnh Dương Hoan - 2264251
- Trần Thái Hà - 22636801
## Mô tả 
- Blog app là một ứng dụng viết blog đơn giản. Ứng dụng này cho phép người dùng đăng ký, đăng nhập, đăng tải nội dung và quản lý các blog cá nhân cũng như là xem được các blog mà những người khác đăng tải. Đây là một project cơ bản để học tập git, django,...
## Hướng dẫn cài đặt, chạy:

### Dùng script
- Chạy script `install.sh` để cài đặt môi trường và chạy ứng dụng

#### Trên Linux
```bash
git clone https://github.com/TrinhDuongHoan/flask-tiny-app.git
```

```bash
cd flask-tiny-app\scripts
```

```bash
./install.sh
```

#### Trên Windows
```bash
git clone https://github.com/TrinhDuongHoan/flask-tiny-app.git
```

```bash
cd flask-tiny-app\scripts
```

```bash
install.bat
```

### Dùng Docker
- Chạy lệnh sau để build và chạy ứng dụng
```bash
git clone https://github.com/TrinhDuongHoan/flask-tiny-app.git
```

```bash
cd flask-tiny-app
```

```bash
docker build -t blog-app .
```

```bash
docker run -p 8000:8000 --name flask-tiny-app blog-app
```

## Link project đã triển khai
- [localhost:8000](http://127.0.0.1:8000/)