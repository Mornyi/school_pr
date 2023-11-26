from django.urls import path
from .views import CustomLoginView, register
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path("register/", register, name="register"),
]