from __future__ import unicode_literals

from django.db import models


class Result(models.Model):
    count = models.CharField(max_length=225)
    key = models.CharField(max_length=225)


class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image_url = models.CharField(max_length=1000)
    key = models.CharField(max_length=225)
    page = models.CharField(max_length=225)