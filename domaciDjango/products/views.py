from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages


def product_list(request):
    products = Product.objects.all().order_by('date')
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required(login_url="/users/login/")
def product_add(request):
    if request.method == 'POST':
        form = forms.addProduct(request.POST, request.FILES)
        if form.is_valid:
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.info(request, 'Uspesno ste objavili oglas!')
            return redirect('products:list')
    else:
        form = forms.addProduct()
    return render(request, 'products/product_add.html', {'form': form})
