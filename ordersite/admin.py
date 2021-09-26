from django.contrib import admin
from django.db import models
from import_export import resources
from import_export.admin import ImportExportMixin

from .models import Product, Size, Offer

admin.site.register(Product)
admin.site.register(Size)

class OfferResource(resources.ModelResource):
  class Meta:
    model = Offer

@admin.register(Offer)
class OfferAdmin(ImportExportMixin, admin.ModelAdmin):
  ordering = ['id']
  list_display = ('購入者', 'メールアドレス', '品名', 'サイズ', '数量', '小計')

  resource_class = OfferResource
