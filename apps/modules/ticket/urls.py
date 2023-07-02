from django.urls import path
from .views import tickets, ticket_detail, ticket_new

urlpatterns = [
    path('', tickets, name='tickets'),
    path('<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('new/', ticket_new, name='ticket_new'),
]