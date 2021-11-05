from django.contrib import admin
from django.db import models
from import_export import resources
from import_export.admin import ImportExportMixin
from rangefilter.filters import DateRangeFilter
from adminsortable.admin import SortableAdmin

from .models import Product, Size, Offer

admin.site.register(Product, SortableAdmin)
admin.site.register(Size)

class ProductAdmin(SortableAdmin):
  list_display = ('品名', '品番', '価格')

class OfferResource(resources.ModelResource):
  class Meta:
    model = Offer

@admin.register(Offer)
class OfferAdmin(ImportExportMixin, admin.ModelAdmin):
  ordering = ['-日付']
  list_display = ('購入者', '日付', 'メールアドレス', '品名', 'サイズ', '数量', '小計')
  list_filter = (
    ('日付', DateRangeFilter),
  )

  resource_class = OfferResource
