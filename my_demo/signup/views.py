from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('register_success')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def register_success(request):
    return render(request, 'register_success.html')


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user