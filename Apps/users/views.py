from django.shortcuts import render
from .forms import AuthenticationForm, UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views import View
from .models import User
from django.contrib import messages

# CVB para el Login 
class CustomLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicia sesión en Diagnosticapp'
        return context

# CVB para el Registro
class CustomSignUp(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/signup'
    success_message = 'Registrado correctamente'

    def get_context_data(self, *args, **kwargs):
        context = super(CustomSignUp, self).get_context_data(*args, **kwargs)
        context['title'] = 'Registrate en Diagnosticapp'
        return context

# CVB para el Logout
class CustomLogout(LogoutView):
    next_page = 'login'

# CVB para el reseteo de la contraseña
class CustomResetPassword(View):
    form_class = PasswordChangeForm
    template_name = 'password.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            user=request.user
        )
        return render(request, 'change_password.html', {
            'form': form,
            'title': 'Cambio de contraseña'
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Contraseña cambiada correctamente')

        return render(request, 'change_password.html', {
            'form': form,
            'title': 'Cambio de contraseña'
        })

        queryset = User.objects.filter(is_superuser=False)
        return queryset

# CVB para la pagina de Home
class Home(TemplateView):
    template_name = "home.html"

# CVB para la pagina de Diagnostico Genera
class dGeneral(TemplateView):
    template_name = "home.html"

# CVB para la pagina de Diagnostico Especifico
class dEspecifico(TemplateView):
    template_name = "home.html"