from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.core.models import Issues


def homepage(request):
    return render(request, 'user/main/homepage.html', {})


def issues(request):
    issue_list = Issues.objects.all().order_by('-id')
    return render(request, 'user/main/issues.html', {
        'issues': issue_list
    })


def privacy_policy(request):
    return render(request, 'user/main/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'user/main/terms_of_use.html')
