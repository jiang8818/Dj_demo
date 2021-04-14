# *_* coding: utf-8 *_*
# time:2021-04-148:07
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # http://127.0.0.1:8000/password/reset/
    re_path(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
            name='password_reset'),

    # http://127.0.0.1:8000/password/reset/done/
    re_path(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
            name='password_reset_done'),

    # http://127.0.0.1:8000/password/reset/user/user-password/
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,50})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='password_reset_confirm.html'),
            name='password_reset_confirm'),
    # http://127.0.0.1:8000/password/reset/complete/
    re_path(r'^reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
            name='password_reset_complete'),

    # 更改密码

    re_path(r'^change/$', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'),
            name='password_change'),

    re_path(r'^change/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
            name='password_change_done'),
]
