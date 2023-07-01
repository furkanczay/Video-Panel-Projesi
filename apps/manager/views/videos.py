from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.core.models import Videos
from apps.manager.forms.videos import VideoForm


@login_required()
@staff_member_required()
def videos_page(request):
    videos = Videos.objects.all()
    return render(request, 'manager/videos/list.html', {
        'videos': videos
    })


@login_required()
@staff_member_required()
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video başarıyla kaydedildi')
            return redirect('admin_videos_page')
    else:
        form = VideoForm()
    return render(request, 'manager/videos/create.html', context={
        'form': form
    })


@login_required()
@staff_member_required()
def video_update(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video başarıyla güncellendi')
            return redirect('admin_videos_page')
    else:
        form = VideoForm(instance=video)
    return render(request, 'manager/videos/update.html', context={
        'form': form
    })


@login_required()
@staff_member_required()
def video_delete(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    video.delete()
    messages.success(request, 'Video başarıyla silindi')
    return redirect('admin_videos_page')
