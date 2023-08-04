import json

from django.shortcuts import render, redirect, get_object_or_404
from apps.core.models import Videos, VideoComments
from django.contrib import messages
from apps.core.forms.videos_forms import VideoFilterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

@login_required()
def videos_list(request):
    videos = Videos.objects.all().order_by('-id')
    paginator = Paginator(videos, 8)
    page_number = request.GET.get('page')

    title = request.GET.get('title')
    print(title)
    if title:
        videos = videos.filter(title__contains=title)
        paginator = Paginator(videos, 8)
    form = VideoFilterForm(request.GET)
    if form.is_valid():

        course = form.cleaned_data.get('course')
        instructor = form.cleaned_data.get('instructor')
        classroom = form.cleaned_data.get('classroom')

        if course:
            videos = videos.filter(classroom__course=course)
            paginator = Paginator(videos, 8)
        if instructor:
            videos = videos.filter(instructor=instructor)
            paginator = Paginator(videos, 8)
        if classroom:
            videos = videos.filter(classroom=classroom)
            paginator = Paginator(videos, 8)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        videos = videos
        video_list = [video.title for video in videos]
        print(video_list)
        json_videos = json.dumps(video_list)
        json_videos = json.loads(json_videos)
        return JsonResponse({'videos': json_videos})
    return render(request, 'user/videos/list.html', {
        'videos': paginator.get_page(page_number),
        'form': form,
    })


@login_required()
def video_detail(request, slug):
    video = get_object_or_404(Videos, slug=slug)
    comments = video.comments.all().order_by('-id')
    all_videos = video.classroom.videos.all().order_by('-id')
    is_video_favorite = request.user.video_favorites.filter(video=video).exists()
    return render(request, 'user/videos/video_detail.html', {
        'video': video,
        'comments': comments,
        'all_videos': all_videos,
        'is_video_favorite': is_video_favorite,
    })


@login_required()
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


@login_required()
def video_comment_update(request, pk):
    video_comment = get_object_or_404(VideoComments, pk=pk)
    if request.method == 'POST':
        if video_comment.author == request.user:
            comment = request.POST.get('comment')
            video_comment.comment = comment
            video_comment.save()
            messages.success(request, 'Yorum başarıyla güncellendi')
            return redirect('video_detail', pk=video_comment.video.pk)


@login_required()
def video_comment_delete(request, pk):
    video_comment = get_object_or_404(VideoComments, pk=pk)
    if video_comment.author == request.user or video_comment.video.instructor == request.user:
        video_comment.delete()
        messages.success(request, 'Yorum başarıyla silindi')
        return redirect('video_detail', pk=video_comment.video.pk)
    else:
        messages.error(request, 'Başkasının yorumunu silemezsiniz')
        return redirect('video_detail', pk=video_comment.video.pk)
