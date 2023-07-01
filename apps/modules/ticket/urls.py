from django.urls import path
from .views import tickets, ticket_detail

urlpatterns = [
    path('', tickets, name='tickets'),
    path('<int:ticket_id>/', ticket_detail, name='ticket_detail'),
]