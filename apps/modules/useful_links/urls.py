from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include([
        path('', useful_links, name='useful_links'),
    ])),
]