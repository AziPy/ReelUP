from django.db import models

from app.users.models import User


class Reel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reels'
    )
    video = models.FileField(
        upload_to='reels/videos/'
    )
    caption = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_reels',
        blank=True
    )

    def __str__(self):
        return f"Reel by {self.user.username} at {self.created_at}"

