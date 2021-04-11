from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

# Create your models here.


class MainUserManager(BaseUserManager):
    """
    Main user manager
    """

    def create_user(self, username, password=None, is_active=None, **kwargs):
        """
        Creates and saves a user with the given username and password
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        if is_active is not None:
            user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password
        """
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Author(AbstractUser):
    username = models.CharField(max_length=100, blank=False,
                                unique=True, db_index=True, verbose_name='Никнейм', null=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    password = models.CharField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    verified = models.BooleanField(default=False)

    objects = MainUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ConfirmCode(models.Model):
    code = models.CharField(max_length=5, verbose_name='Код подтверждения')
    confirm = models.BooleanField(default=False)
    reset = models.BooleanField(default=False)
    author = models.ForeignKey(
        Author, related_name="codes", on_delete=models.CASCADE, verbose_name='Пользователь')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(5)
        super(ConfirmCode, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'
