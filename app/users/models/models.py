from django.db import models
from .user import User


def user_profile_image_path(instance, filename):
    return f'user/profile/images/{instance.user.id}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_profile_image_path
    )
    full_name = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    birth_date = models.DateField(
        null=True,
        blank=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField('User', related_name='following', blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"





