from django.urls import path
from catalog.views import main_page, contact_page, items_page, item_detail


urlpatterns = [
    path('', main_page, name='main_page'),
    path('main/', main_page, name='main_page'),
    path('contacts/', contact_page, name='contact_page'),
    path('items/', items_page, name='items_page'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
]

