from django.urls import path, include
from .views import main

urlpatterns = [
    path('', include([
        path('', main.dashboard, name='admin_dashboard'),
    ]))
]
