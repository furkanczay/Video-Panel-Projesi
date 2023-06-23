from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.decorators import group_required
from apps.core.forms.instructor_forms import VideoUpload
from django.contrib import messages


@login_required()
@group_required('Eğitmen')
def instructor_panel(request):
    videos = request.user.videos.all().order_by('-id')
    return render(request, 'user/instructors/instructor_panel.html', {
        'videos': videos
    })


@login_required()
@group_required('Eğitmen')
def video_upload(request):
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.instructor = request.user
            video.save()
            messages.success(request, 'Video başarıyla yüklendi')
            return redirect('instructor_panel')
    else:
        form = VideoUpload()
    return render(request, 'user/instructors/video_upload.html', {
        'form': form
    })
