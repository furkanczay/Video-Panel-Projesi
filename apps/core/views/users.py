from django.shortcuts import render


# PROFILE VIEWS
def profile(request):
    user = request.user
    return render(request, 'user/users/profile.html', {
        'user': user
    })
