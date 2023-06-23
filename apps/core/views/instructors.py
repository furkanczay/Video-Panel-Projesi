from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.core.decorators import group_required


@group_required('Eğitmen')
def instructor_panel(request):
    videos = request.user.videos.all().order_by('-id')
    return render(request, 'user/instructors/instructor_panel.html', {
        'videos': videos
    })
