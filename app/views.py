from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UserPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostDeleteForm
from .forms import PostForm


# Trang chủ
def home(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 10) 

    page_number = request.GET.get('page') 
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)

    return render(request, 'user_posts.html', {'user': user, 'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Gán user hiện tại làm chủ bài viết
            post.save()
            return redirect('user_posts', username=request.user.username)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect('user_posts', username=request.user.username)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_posts', username=request.user.username)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect('user_posts', username=request.user.username)

    post.delete()
    return redirect('user_posts', username=request.user.username)

@login_required
def delete_multiple_posts(request):
    if request.method == "POST":
        post_ids = request.POST.getlist("post_ids") 

        if post_ids:
            posts = Post.objects.filter(pk__in=post_ids, user=request.user) 
            posts.delete()

            messages.success(request, "✅ Selected posts have been deleted successfully!")
        else:
            messages.error(request, "❌ Please select at least one post to delete.")

    return redirect("user_posts", username=request.user.username)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


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

