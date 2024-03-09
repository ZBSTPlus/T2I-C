from django.db import models

class TextToImage(models.Model):
    text = models.TextField()
    font_size = models.IntegerField()
