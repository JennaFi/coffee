from django.shortcuts import render
from .models import Coffee, Tea


def index(request):
    coffee = Coffee.objects.filter(sale=True)
    tea = Tea.objects.filter(sale=True)

    return render(request,
                 'shop/index.html',
                 {'coffee': coffee,
                  'tea': tea})


def coffee_list(request):
    coffee = Coffee.objects.all()

    return render(request,
                  'shop/coffee.html',
                  {'coffee': coffee})


def tea_list(request):
    tea = Tea.objects.all()

    return render(request,
                  'shop/tea.html',
                  {'tea': tea})


#def product_detail(request, id, slug):
