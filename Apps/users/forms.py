from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django import forms


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Usuario'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña'}) 
        self.fields['password'].label = False


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'is_superuser', 'is_staff', 'email']
        widgets = {
            'is_superuser': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
            'email': forms.HiddenInput()
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'is_superuser', 'is_staff']:
            self.fields[fieldname].help_text = None
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Elíge un nombre de usuario'})
        self.fields['username'].label = False
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña'}) 
        self.fields['password1'].label = False
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña nuevamente'}) 
        self.fields['password2'].label = False

    def save(self, commit=True):
        if self.instance.email == '':
            self.instance.email = None
        return super().save(commit=commit)
