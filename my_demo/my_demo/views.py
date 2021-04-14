# *_* coding: utf-8 *_*
# time:2021-04-0915:39
# tools:PyCharm
# file_name：views.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

