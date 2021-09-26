from django.urls import path
from . import views

urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('post/new/', views.post_new, name='post_new'),
  path('confirmation/', views.move_to_confirmation, name='move_to_confirmation'),
  path('completion', views.completion, name='completion'),
  path('error', views.error, name='error'),
]
