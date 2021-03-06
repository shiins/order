from django.shortcuts import render
from .models import Swimsuit

def total_price(request):
  # total_price = Swimsuit.total_price.get()
  total_price = '10000' 
  return render(request, 'ordersite/order.html', {'total_price': total_price})