from django.urls import path, include
from .views import main

urlpatterns = [
    path('', include([
        path('', main.dashboard, name='admin_dashboard'),
        path('general-settings/', main.general_settings, name='admin_general_settings'),
    ]))
]
