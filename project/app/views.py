from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .models import Product
from datetime import datetime
from .forms import ProductForm

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', context={'product': product})


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            view = form.cleaned_data['view']
            price = form.cleaned_data['price']
            Product.objects.create(name=name, view=view, price=price)
            return redirect('home')

    form = ProductForm()
    return render(request, 'create.html', context={'form': form})


def update(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            product.name = request.POST.get('name')
            product.age = request.POST.get('age')
            product.price = request.POST.get('price')
            product.save()
            return redirect('home')
        else:
            return render(request, 'update.html', context={'product': product})
    except:
        return redirect('home')


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('home')
    except:
        return redirect('home')



