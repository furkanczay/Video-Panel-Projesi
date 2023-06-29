from django.urls import path, include
from .views import users, main, instructors, videos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include([
        path('', main.homepage, name='homepage'),
        path('privacy-policy/', main.privacy_policy, name='privacy_policy'),
        path('terms-of-use/', main.terms_of_use, name='terms_of_use'),
        # USER URLS
        path('login/', users.login_page, name='login'),
        path('login-validate/', users.login_validate, name='login_validate'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('profile/', users.profile, name='profile'),
        path('profile/update/', users.profile_update, name='profile_update'),
        path('favorite_video/<int:pk>/', users.favorite_video, name='favorite_video'),
        path('favorite-videos/', users.favorite_videos, name='favorite_videos'),
        # INSTRUCTOR URLS
        path('instructor-panel/', include([
            path('', instructors.instructor_panel, name='instructor_panel'),
            path('video-upload/', instructors.video_upload, name='video_upload'),
            path('video-edit/<int:pk>/', instructors.video_edit, name='video_edit'),
            path('video-delete/<int:pk>/', instructors.video_delete, name='video_delete'),
        ])),
        # VIDEOS URLS
        path('videos/', include([
            path('', videos.videos_list, name='videos_list'),
            path('<int:pk>/', videos.video_detail, name='video_detail'),
            path('comments/create/', videos.video_comment_create, name='video_comment_create'),
            path('comments/delete/<int:pk>/', videos.video_comment_delete, name='video_comment_delete'),
            path('comments/update/<int:pk>/', videos.video_comment_update, name='video_comment_update'),
        ])),
    ])),
]
