from django.urls import path
from catalog.views import contact_page, items_page, ProductListView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView
from catalog.views import BlogUpdateView, BlogDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', ProductListView.as_view(), name='main_page'),
    path('main/', ProductListView.as_view(), name='main_page'),
    path('contacts/', contact_page, name='contact_page'),
    path('items/', items_page, name='items_page'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='item_detail'),

    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('read/', BlogListView.as_view(), name='read_blog'),  # we read all blog
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),  # here we read only one publication
]
