from django.db import models


class UploadModel(models.Model):
    upload_file = models.ImageField()
