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
  price = models.IntegerField(name='価格')
  sizes = models.ManyToManyField(Size)
  size = models.CharField(name='サイズ', max_length=20, blank=True, editable=False)
  num = models.IntegerField(name='数量', default=0, editable=False)
  image = models.ImageField(upload_to='documents/', default='defo')

  def __str__(self):
    return self.品名

class Offer(models.Model):
  purchaser = models.CharField(name='購入者', max_length=20, null=True)
  email = models.EmailField(name='メールアドレス', null=True)

  name = models.CharField(name='品名', max_length=20, null=True, blank=True)
  id = models.CharField(name='品番', max_length=20, null=True, blank=True)
  price = models.IntegerField(name='価格', null=True, blank=True)
  size = models.CharField(name='サイズ', max_length=20, null=True, blank=True)
  quantity = models.IntegerField(name='数量', null=True, blank=True)
  subtotal = models.IntegerField(name='小計', null=True, blank=True)

  def save(self, *args, **kwargs):
    self.小計 = self.価格 * self.数量
    super(Offer, self).save(*args, **kwargs)

  def __str__(self):
    return str(self.購入者)
