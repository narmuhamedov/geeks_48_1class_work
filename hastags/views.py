from django.shortcuts import render
from . import models

#общий список продуктов
def all_products(request):
    if request.method == "GET":
        all_products = models.Product.objects.all()
        context = {'all_products': all_products}
        return render(request, template_name='hastags/all_products.html', 
                      context=context)

#список на напитки 
def drink_product(request):
    if request.method == "GET":
        drink_product = models.Product.objects.filter(tags__name='Напитки')
        context = {'drink_product': drink_product}
        return render(request, template_name='hastags/drink_products.html',
                      context=context)
    
#список на напитки 
def eat_product(request):
    if request.method == "GET":
        eat_product = models.Product.objects.filter(tags__name='Еда')
        context = {'eat_product': eat_product}
        return render(request, template_name='hastags/eat_products.html',
                      context=context) 