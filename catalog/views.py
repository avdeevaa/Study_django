from django.shortcuts import render, reverse
from catalog.models import Product, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    """ replaces main_page"""
    model = Product
    template_name = 'design/main_page.html'


# def main_page(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'design/main_page.html', context)


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


class ProductDetailView(DetailView):
    """ replaces item_detail"""
    model = Product
    template_name = 'design/item_detail.html'

#
# def item_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'design/item_detail.html', context)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'creation_date', 'publication_sign')
    template_name = 'design/blog_form.html'

    def get_success_url(self):
        return reverse('catalog:read_blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'creation_date')
    template_name = 'design/blog_form.html'

    def get_success_url(self):
        return reverse('catalog:read_blog')


class BlogListView(ListView):
    model = Blog
    template_name = 'design/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'design/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'design/blog_confirm_delete.html'

    def get_success_url(self):
        return reverse('catalog:read_blog')
