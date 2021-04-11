from django.shortcuts import render

from .models import Author, ConfirmCode
from .forms import (
    AuthorRegisterForm, LoginForm, ResetPasswordForm
)
from .utils import (
    send_verifiy_link, send_password_reset_link
)


# Регистрация
def register(request):
    form = AuthorRegisterForm
    if request.method == 'POST':
        save_form = AuthorRegisterForm(request.POST)
        # Если пользователь уже зарегался
        if Author.objects.filter(email=request.POST['email'], verified=False):
            author = Author.objects.get(email=request.POST['email'])
            author.codes.all().delete()
            code = ConfirmCode.objects.create(author=author)
            send_verified_link(
                f'Чтобы подтвердить почту, перейдите по ссылке http://127.0.0.1:8000/auth/{code.code}/', code.author.email)
            return render(request, 'reply.html', context={'message': 'Проверьте вашу почту'})

        # Обычная регистрация
        if save_form.is_valid():
            author = Author.objects.create(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
            )
            code = ConfirmCode.objects.create(author=author)
            send_verified_link.delay(
                f'Чтобы подтвердить почту, перейдите по ссылке /{code.code}/', code.author.email)
            return render(request, 'reply.html', context={'message': 'Проверьте вашу почту'})
        return render(request, 'reply.html', context={'form': form, 'errors': save_form.errors})
    return render(request, 'register.html', context={'form': form})


# Подтверждение кода
def confirm(request, code):
    if ConfirmCode.objects.filter(code=code):
        code = ConfirmCode.objects.get(code=code)
        if not code.confirm:
            code.confrim = True
            code.save()
            code.author.verified = True
            code.author.save()
            return render(request, 'reply.html', {'message': 'Ваша почта подтверждена', 'success': True})
        return render(request, 'reply.html', {'message': 'Ваша почта уже подтверждена', 'success': True})
    return render(request, 'reply.html', {'message': 'Ваш код устарел, либо неправильный', 'success': True})


# Логин
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        if Author.objects.filter(username=request.POST['username'], password=request.POST['password']):
            return render(request, 'reply.html', {'message': 'Вы вошли в аккаунт', 'success': True})
        else:
            return render(request, 'login.html', context={'message': 'Неправильный никнейм или пароль', 'success': True})
    return render(request, 'login.html', context={'form': form})


# Сброс пароля
def reset_password(request):
    form = ResetPasswordForm()
    if request.method == 'POST':
        author = Author.objects.filter(email=request.POST['email'])
        if author:
            code = ConfirmCode.objects.create(author=author.last(), reset=True)
            send_verified_link(
                f'Чтобы подтвердить почту для сброса пароля, перейдите по ссылке - http://127.0.0.1:8000/auth/confirm/password/{code.code}/', code.author.email)
            return render(request, 'reply.html', {'message': 'Проверьте вашу почту', 'success': True})
        return render(request, 'reply.html', {'message': 'Ваш код устарел, либо неправильный', 'success': True})
    return render(request, 'reset_password.html', context={'form': form})
