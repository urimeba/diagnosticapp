from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, user_passes_test
from . import views
from .decorators.custom_decorators import anonymous_required

urlpatterns = [
    # URLS para el uso de los usuarios normales
    path('', views.CustomLogin.as_view(), name='login'),
    path('signup', anonymous_required(views.CustomSignUp.as_view()) , name='signup'),
    path('home',login_required(views.Home.as_view()), name='home'),
]
