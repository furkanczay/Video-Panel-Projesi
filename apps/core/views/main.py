from django.shortcuts import render
from apps.core.models import Issues, Users


def homepage(request):
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return render(request, 'user/main/homepage.html', {
        'instructors': instructors
    })


def issues(request):
    issue_list = Issues.objects.all().order_by('-id')
    return render(request, 'user/main/issues.html', {
        'issues': issue_list
    })


def privacy_policy(request):
    return render(request, 'user/main/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'user/main/terms_of_use.html')
