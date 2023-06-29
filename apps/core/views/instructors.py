from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.decorators import group_required
from apps.core.forms.instructor_forms import VideoUpload
from django.contrib import messages


@login_required()
@group_required('Eğitmen')
def instructor_panel(request):
    classrooms = request.user.instructor_classrooms.all()
    videos = request.user.instructor_videos.all().order_by('-id')[:5]
    return render(request, 'user/instructors/instructor_panel.html', {
        'videos': videos
    })


@login_required()
@group_required('Eğitmen')
def video_upload(request):
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            video = form.save(commit=False)
            video.instructor = request.user
            video.save()
            messages.success(request, 'Video başarıyla yüklendi')
            return redirect('instructor_panel')
    else:
        form = VideoUpload(user=request.user)
    return render(request, 'user/instructors/video_upload.html', {
        'form': form
    })


@login_required()
@group_required('Eğitmen')
def video_edit(request, pk):
    video = request.user.instructor_videos.get(pk=pk)
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES, user=request.user, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video başarıyla güncellendi')
            return redirect('instructor_panel')
    else:
        form = VideoUpload(user=request.user, instance=video)
    return render(request, 'user/instructors/video_edit.html', {
        'form': form
    })


def video_delete(request, pk):
    video = request.user.instructor_videos.get(pk=pk)
    video.delete()
    messages.success(request, 'Video başarıyla silindi')
    return redirect('instructor_panel')
