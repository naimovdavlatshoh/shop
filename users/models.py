from pyexpat import model
from statistics import mode
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from . manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField('First name', blank=True, null=True, max_length=250)
    last_name = models.CharField('Last name', blank=True, null=True, max_length=250)
    date = models.DateTimeField('Дата рождения', blank=True,null=True)
    image = models.ImageField('Фото', blank=True, null=True)
    gender = models.CharField('Пол', max_length=256, blank=True,null=True)
    number = models.CharField('Номер телефона', blank=True, null=True, max_length=256)
    pasport  = models.CharField('Серия Паспорта', max_length=256, null=True)
    address = models.CharField('Адрес', max_length=256,null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Указано, что все объекты для класса поступают из CustomUserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.email