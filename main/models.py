from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    user_choice = [('p', 'Photo'), ('f', 'Document'), ('l', 'Link')]
    file_type = models.CharField(max_length=6, choices=user_choice, default='Link')
    document = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    #user_id = models.IntegerField("User id", blank=False, default=2)
