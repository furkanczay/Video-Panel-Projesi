from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


@login_required()
def homepage(request):
    return render(request, 'user/main/homepage.html', {})
