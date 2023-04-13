from django.conf.urls.static import static
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import path, reverse_lazy, reverse
from django.views.generic import CreateView
from . import views
from .forms import LoginUserForm
from django.conf import settings

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'

    def get_success_url(self):
        return reverse("home")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse("home")


def logout_user(request):
    logout(request)
    return redirect('login')


urlpatterns = [
    # path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create-news', views.create, name='create'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('', views.aviata, name = 'home'),
    path('feedback', views.index, name = 'feedback'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
