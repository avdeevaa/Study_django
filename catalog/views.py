from django.shortcuts import render, get_object_or_404
# Create your views here.

from catalog.models import Product

# def main_page(request):
#     return render(request, 'design/main_page.html')


def main_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'design/main_page.html', context)


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Форма обрабатывает {name}, {phone}, {message}")
    return render(request, 'design/contact_page.html')


def items_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'design/items_page.html', context)


def item_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'design/item_detail.html', context)


