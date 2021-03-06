from django.urls import path
from . import views

urlpatterns = [
  path('', views.total_price, name='total_price'),
]