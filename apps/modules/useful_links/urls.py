from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include([
        path('', useful_links, name='useful_links'),
        path('add/', useful_links_add, name='useful_links_add'),
        path('edit/<int:pk>/', useful_links_edit, name='useful_links_edit'),
        path('delete/<int:pk>/', useful_links_delete, name='useful_links_delete'),
    ])),
]