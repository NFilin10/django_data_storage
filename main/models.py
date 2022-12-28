from django.db import models

class Document(models.Model):
    # user_choice =  [
    # ('p', 'Phtot'),
    # ('f', 'File')]
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
