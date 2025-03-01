from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UserPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

# Trang chủ
def home(request):
    return render(request, 'home.html')

# View đăng ký
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Đăng ký thành công! Vui lòng đăng nhập.")
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

# View đăng nhập
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.is_active:
                messages.error(request, "🔒 Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ quản trị viên.")
                return redirect('login')
            
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "❌ Tên đăng nhập hoặc mật khẩu không đúng.")      
        else:
            messages.error(request, "❌ Tên đăng nhập hoặc mật khẩu không đúng.")  
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# View đăng xuất
def logout_view(request):
    logout(request)
    messages.success(request, "👋 Bạn đã đăng xuất thành công.")
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Giữ session đăng nhập
            messages.success(request, "✅ Mật khẩu đã được thay đổi thành công!")
            return render(request, 'password_success.html')
        else:
            messages.error(request, "❌ Có lỗi xảy ra, vui lòng kiểm tra lại thông tin.")
    else:
        form = UserPasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})

