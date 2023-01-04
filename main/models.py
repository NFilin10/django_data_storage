from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    # user_choice =  [
    # ('p', 'Phtot'),
    # ('f', 'File')]
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    #user_id = models.IntegerField("User id", blank=False, default=2)
