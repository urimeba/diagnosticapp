from django.conf.urls import url
from django.urls import path, include
from . import views as views_diagnostico


urlpatterns = [
    path('', views_diagnostico.Home.as_view(), name="home"),
]
