from django.shortcuts import render
from .forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, FormView, UpdateView

# Create your views here.
class CustomLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicia sesión en Diagnosticapp'
        return context


class CustomSignUp(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/signup'
    success_message = 'Usuario creado correctamente'

    def get_initial(self):
        initial = super(CustomSignUp, self).get_initial()
        initial = initial.copy()
        initial['is_superuser'] = False
        initial['is_staff'] = False
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super(CustomSignUp, self).get_context_data(*args, **kwargs)
        context['title'] = 'Registrate en Diagnosticapp'
        return context