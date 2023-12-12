from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('user:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    
