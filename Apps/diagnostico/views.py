from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

# class dGeneral(TemplateView):
#     template_name = "home.html"

# class dEspecifico(TemplateView):
#     template_name = "home.html"