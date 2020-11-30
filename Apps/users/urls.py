from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .decorators.custom_decorators import anonymous_required

urlpatterns = [
    path('', views.CustomLogin.as_view(), name='login'),
    path('logout', login_required(views.CustomLogout.as_view()), name='logout'),
    path('signup', anonymous_required(views.CustomSignUp.as_view()) , name='signup'),
    path('password', login_required(views.CustomResetPassword.as_view()), name="change_password"),
    path('home',login_required(views.Home.as_view()), name='home'),
    path('dGeneral', login_required(views.dGeneral.as_view()), name="dGeneral"),
    path('dEspecifico', login_required(views.dEspecifico.as_view()), name="dEspecifico"),
]
