from django.contrib import admin
from app.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')  
    list_filter = ('is_active',)  
    search_fields = ('username', 'email')

    actions = ['disable_users', 'enable_users']

    # Action để disable user
    def disable_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Đã vô hiệu hóa người dùng thành công.")
    disable_users.short_description = "Disable các user đã chọn"

    # Action để enable user
    def enable_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Đã kích hoạt lại người dùng thành công.")
    enable_users.short_description = "Enable các user đã chọn"



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


    





