from django.shortcuts import render, redirect, get_object_or_404
from apps.core.models import Videos, VideoComments
from django.contrib import messages


def video_detail(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    comments = video.comments.all().order_by('-id')
    all_videos = video.classroom.videos.all().order_by('-id')
    return render(request, 'user/videos/video_detail.html', {
        'video': video,
        'comments': comments,
        'all_videos': all_videos
    })


def video_comment_update(request):
    pass


def video_comment_delete(request, pk):
    video_comment = get_object_or_404(VideoComments, pk=pk)
    if video_comment.author == request.user:
        video_comment.delete()
        messages.success(request, 'Yorum başarıyla silindi')
        return redirect('video_detail', pk=video_comment.video.pk)
