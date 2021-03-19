from django.conf import settings
from django.db import models
from django.utils import timezone

class Size(models.Model):
  size = models.CharField(max_length=20)

  def __str__(self):
    return self.size

class Product(models.Model):
  name = models.CharField(name='品名', max_length=20)
  id = models.CharField(name='品番', max_length=20)
  price = models.IntegerField(name='価格', default=10000)
  sizes = models.ManyToManyField(Size)
  size = models.CharField(name='サイズ', max_length=20, blank=True)
  num = models.IntegerField(name='数量')
  image = models.ImageField(upload_to='documents/', default='defo')

  def __str__(self):
    return self.品名

class Offer(models.Model):
  name = models.CharField(name='名前', max_length=20)

  def __str__(self):
    return self.名前
