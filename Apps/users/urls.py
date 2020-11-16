from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, user_passes_test
from . import views

urlpatterns = [
    # URLS para el uso de los usuarios normales
    path('', views.CustomLogin.as_view(), name='login'),
    path('signup', views.CustomSignUp.as_view(), name='signup'),
]
