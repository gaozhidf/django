from django.db import models
from .fields import CompressedTextField, ListField


class Article(models.Model):
    labels = ListField()
    content = CompressedTextField(null=True, default='')
