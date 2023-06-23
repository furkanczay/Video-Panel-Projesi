from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.core.models import Issues


@login_required()
def homepage(request):
    return render(request, 'user/main/homepage.html', {})


@login_required()
def issues(request):
    issue_list = Issues.objects.all().order_by('-id')
    return render(request, 'user/main/issues.html', {
        'issues': issue_list
    })
