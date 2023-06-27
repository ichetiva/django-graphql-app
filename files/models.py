from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    lines_count = models.IntegerField(null=True)
