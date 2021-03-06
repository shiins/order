from django.conf import settings
from django.db import models
from django.utils import timezone

class Swimsuit(models.Model):
  name = models.CharField(name='品名', max_length=20)
  id = models.CharField(name='品番', max_length=20)
  price = models.IntegerField(name='価格')
  total_price = models.IntegerField(name='合計価格')
  size = models.CharField(name='サイズ', max_length=20)
  num = models.IntegerField(name='着数')

  # 合計価格の算出
  def cal_total_price(self):
    self.total_price = self.price * self.num
