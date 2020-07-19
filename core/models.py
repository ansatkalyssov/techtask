from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models
import os


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField('Age', blank=True, null=True)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    avatar = models.FileField('Avatar', upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.username


@receiver(models.signals.pre_delete, sender=Profile)
def delete_avatar(sender, instance, **kwargs):
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)


@receiver(models.signals.pre_save, sender=Profile)
def hash_user_password(sender, instance, **kwargs):
    instance.set_password(instance.password)
