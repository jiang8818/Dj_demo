# *_* coding: utf-8 *_*
# time:2021-04-1317:01
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#


from django.urls import path, include, re_path
from signup import views as signup_view

from django.contrib.auth import views as auth_views

urlpatterns = [
    # 127.0.0.1:8000/signup/login  登录页面
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 127.0.0.1:8000/signup/register    注册用户
    path('register/', signup_view.register, name='register'),
    # 127.0.0.1:8000/signup/logout    注销登录
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register_success/',signup_view.register_success,name='register_success'),

    re_path(r'^account/$',signup_view.UserUpdateView.as_view(),name='my_account'),
]
