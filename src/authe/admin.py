from django.contrib import admin

from .models import Author, ConfirmCode

# Register your models here.

admin.site.register(Author)
admin.site.register(ConfirmCode)
