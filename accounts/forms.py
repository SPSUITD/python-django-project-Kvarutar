from django.contrib.auth.models import User
from django import forms

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    """  """
    username = forms.CharField(help_text="Никнейм")
    first_name = forms.CharField(help_text="Имя")
    email = forms.EmailField(help_text="Почта")
    """  """
    password = forms.CharField(help_text='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(help_text='Повторите пароль', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


