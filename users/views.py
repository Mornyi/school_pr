from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('login')  # Замените 'home' на URL вашей главной страницы
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    