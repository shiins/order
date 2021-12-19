import re
from django import forms
from django.db.models.base import Model
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import transaction
from django.core.mail import message, send_mail
from .models import Offer, Product
from .forms import PostForm, PostFormSet

def product_list(request):
  if request.method == "GET":
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'ordersite/order.html', context)

def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('product_list', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'ordersite/post_edit.html', {'form': form})

def move_to_confirmation(request):
  listed_products = {}
  formset = PostFormSet(request.POST or None, queryset=Offer.objects.none())

  if request.method == "POST":
    if formset.is_valid():
      recipient_address = ''
      mes = ""
      i = 0
      for form in formset:
        if not form.__getitem__("品名").value():
          break
        recipient_address = str(form.__getitem__("メールアドレス").value())
        mes += str(form.__getitem__("品名").value()) + "\n"
        i += 1

      # メール送信
      subject = "ご注文いただいた商品のお知らせ"
      message = "この度はご注文いただき誠にありがとうございます。\nご注文いただいた商品は、\n\n" + mes + "\nの" + str(i) + "点になります。"
      from_email = 'kikoh.hirakata@gmail.com'
      recipient_list = [recipient_address]
      send_mail(subject, message, from_email, recipient_list)

      formset.save()
      return redirect('completion')
    return redirect('error')

  else:
    if not request.GET.get('listed_products_length'):
      return redirect('product_list')

    for i in range(int(request.GET.get('listed_products_length'))):
      listed_name = 'listed_name' + str(i)
      listed_size = 'listed_size' + str(i)
      listed_price = 'listed_price' + str(i)
      listed_quantity = 'listed_quantity' + str(i)

      product = 'product' + str(i)

      listed_product = [
        request.GET.get(listed_name),
        request.GET.get(listed_size),
        request.GET.get(listed_price),
        request.GET.get(listed_quantity),
      ]

      listed_products[product] = listed_product

  context = {'listed_products': listed_products, 'formset':formset}
  return render(request, 'ordersite/post_edit.html', context)

def completion(request):
  if request.method == "GET":
    return render(request, 'ordersite/completion.html')

def error(request):
  if request.method == "GET":
    return render(request, 'ordersite/error.html')
