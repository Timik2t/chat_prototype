from django.db import models
from ..users.models import User


class Dialog(models.Model):
    participants = models.ManyToManyField(User, related_name='dialogs')


class Message(models.Model):
    dialog = models.ForeignKey(
        Dialog,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
