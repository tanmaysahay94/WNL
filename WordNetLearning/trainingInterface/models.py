from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Record(models.Model):
    hindi_word = models.CharField(max_length=64, unique=True)
    english_meaning = models.CharField(max_length=128)
    examples = models.CharField(max_length=1024)
    sense = models.IntegerField(null=True)
