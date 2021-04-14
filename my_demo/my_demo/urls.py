"""my_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from my_demo import views
from signup import views as signup_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    # 127.0.0.1:8000    首页
    path('', views.home, name='home'),
    path('hr/',include('hr.urls')),
    path('signup/', include('signup.urls')),
    path('password/',include('password.urls')),


    # 127.0.0.1:8000/register    注册用户
    # path('register/', signup_view.register, name='register'),

    # # 127.0.0.1:8000/login  登录页面
    # path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # # 127.0.0.1:8000/logout  用户注销
    # path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('admin/', admin.site.urls),
]
