from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'design/main_page.html')


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Форма обрабатывает {name}, {phone}, {message}")
    return render(request, 'design/contact_page.html')
