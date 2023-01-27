from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user_choice = [('Link', 'Link'), ('Note', 'Note')]
    file_type = models.CharField(max_length=15, choices=user_choice, default='Link')
    heading = models.CharField(max_length=30, null=True)
    user_data = models.TextField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


#Model for files and pics
class Document(models.Model):
    user_choice = [('Photo', 'Photo'), ('Document', 'Document')]
    file_type = models.CharField(max_length=15, choices=user_choice, default='Link')
    document = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    note_file = models.ManyToManyField(Note, null=True)

