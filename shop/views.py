from django.shortcuts import get_object_or_404, render

from shop.models import Shop, Category, Types

def home(request) :
    return render(request, 'index.html')

def products(request) :
    shops = Shop.objects.all()
    categories = Category.objects.all()
    types = Types.objects.all()
    context = {
        'shops': shops,
        'categories': categories,
        'types': types,
    }
    return render(request, 'products.html', context=context)

def detail(request, pk) :
    shops = get_object_or_404(Shop, id=pk)
    categories = Category.objects.all()
    context = {
        'shops': shops,
        'categories': categories,
    }
    return render(request, 'detail.html', context=context)

