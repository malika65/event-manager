from django import forms

from .models import Author


# Форма для регистрации
class AuthorRegisterForm(forms.ModelForm):
    password = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = Author
        fields = ('email', 'username', 'password')
    username.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш ник'
    })
    email.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваша почта'
    })
    password.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш пароль'
    })


# Форма для логина
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('username', 'password')
    username.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш ник',
    })
    password.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш пароль',
    })


# Форма для сброса пароля
class ResetPasswordForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField()

    class Meta:
        model = Author
        fields = ('username', 'password')
    username.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш ник',
    })
    email.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваша почта',
    })
