from django.urls import path, include
from .views import users, main

urlpatterns = [
    path('', include([
        path('', main.homepage, name='homepage'),
        path('login/', users.login_page, name='login'),
        path('logout/', users.logout_page, name='logout'),
    ])),
]
