from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "🔒 Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ quản trị viên.",
                code='inactive',
            )
            
class AdminPasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150, label="Tên đăng nhập")
    new_password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu mới")
    
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu hiện tại'}),
        label="Mật khẩu hiện tại",
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu mới'}),
        label="Mật khẩu mới",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Xác nhận mật khẩu mới'}),
        label="Xác nhận mật khẩu mới",
    )



