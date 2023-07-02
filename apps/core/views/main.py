from django.shortcuts import render
from apps.core.models import Users
from django.contrib.auth.decorators import login_required


@login_required()
def homepage(request):
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return render(request, 'user/main/homepage.html', {
        'instructors': instructors
    })


@login_required()
def privacy_policy(request):
    return render(request, 'user/main/privacy_policy.html')


@login_required()
def terms_of_use(request):
    return render(request, 'user/main/terms_of_use.html')
