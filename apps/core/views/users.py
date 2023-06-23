from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
# PROFILE VIEWS
def profile(request):
    user = request.user
    return render(request, 'user/users/profile.html', {
        'user': user
    })
