from django.shortcuts import render, get_object_or_404
from apps.core.models import Videos


def video_detail(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    all_videos = video.classroom.videos.all().order_by('-id')
    return render(request, 'user/videos/video_detail.html', {
        'video': video,
        'all_videos': all_videos
    })
