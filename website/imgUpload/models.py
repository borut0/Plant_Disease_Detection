from django.db import models

# Create your models here.
class Files(models.Model):
    imgs = models.FileField(upload_to='file')