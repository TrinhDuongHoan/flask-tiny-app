from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

# View đăng ký
def register_view(request):
    if request.user.is_authenticated:  # Nếu người dùng đã đăng nhập, chuyển hướng họ đến trang home
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công!")
            return redirect('login')  # Sau khi đăng ký xong, chuyển hướng đến trang đăng nhập
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

# View đăng nhập
def login_view(request):
    if request.user.is_authenticated:  # Nếu người dùng đã đăng nhập, chuyển hướng họ đến trang home
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Chào mừng {user.username}!")
            return redirect('home')  # Sau khi đăng nhập thành công, chuyển hướng đến trang home
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Thực hiện đăng xuất người dùng
    return redirect('login')