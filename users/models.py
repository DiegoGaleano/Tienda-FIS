from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    '''
    Modelo de perfil: extendiendo la información del usuario con un modelo proxy
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # email = models.EmailField(max_length=200, required=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    biography = models.TextField(blank = True)
    address = models.CharField(max_length=225, blank=True, null=True)
    address_detail = models.TextField(blank = True)

    picture = models.ImageField(
        upload_to = 'users/picture',
        blank = True,
        null = True
    )

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username

