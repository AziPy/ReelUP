from django.db import models

from app.users.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )



    image = models.ImageField(
        upload_to='posts/images/'
    )



    caption = models.TextField(
        blank=True,
        null=True
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )



    likes = models.ManyToManyField(
        User, related_name='liked_posts',
        blank=True
    )



    dislikes = models.ManyToManyField(
        User,
        related_name='disliked_posts',
        blank=True
    )



    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"