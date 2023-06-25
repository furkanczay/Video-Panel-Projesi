from django.shortcuts import render, redirect, get_object_or_404
from apps.core.models import Videos, VideoComments
from django.contrib import messages
from apps.core.forms.videos_forms import VideoFilterForm


def videos_list(request):
    form = VideoFilterForm(request.GET)
    if form.is_valid():
        course = form.cleaned_data.get('course')
        instructor = form.cleaned_data.get('instructor')

        videos = Videos.objects.all().order_by('-id')

        if course:
            videos = videos.filter(classroom__course=course)
        if instructor:
            videos = videos.filter(instructor=instructor)

    else:
        videos = Videos.objects.all().order_by('-id')
    return render(request, 'user/videos/list.html', {
        'videos': videos,
        'form': form
    })


def video_detail(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    comments = video.comments.all().order_by('-id')
    all_videos = video.classroom.videos.all().order_by('-id')
    return render(request, 'user/videos/video_detail.html', {
        'video': video,
        'comments': comments,
        'all_videos': all_videos
    })


def video_comment_create(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        comment = request.POST.get('comment')
        video_id = request.POST.get('video_id')

        # Gerekli doğrulamaları yap

        # Videoyu bul
        video = Videos.objects.get(id=video_id)

        # Yorumu oluştur ve videoya bağla
        comment = VideoComments.objects.create(author=request.user, comment=comment, video=video)

        # Diğer işlemler (örneğin, yönlendirme veya mesaj gösterme)
        messages.success(request, 'Yorum başarıyla eklendi')
        return redirect('video_detail', pk=video_id)


def video_comment_update(request, pk):
    video_comment = get_object_or_404(VideoComments, pk=pk)
    if request.method == 'POST':
        if video_comment.author == request.user:
            comment = request.POST.get('comment')
            video_comment.comment = comment
            video_comment.save()
            messages.success(request, 'Yorum başarıyla güncellendi')
            return redirect('video_detail', pk=video_comment.video.pk)


def video_comment_delete(request, pk):
    video_comment = get_object_or_404(VideoComments, pk=pk)
    if video_comment.author == request.user:
        video_comment.delete()
        messages.success(request, 'Yorum başarıyla silindi')
        return redirect('video_detail', pk=video_comment.video.pk)
