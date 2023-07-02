from django.urls import path, include
from .views import users, main, instructors, videos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include([
        path('', main.homepage, name='homepage'),
        path('privacy-policy/', main.privacy_policy, name='privacy_policy'),
        path('terms-of-use/', main.terms_of_use, name='terms_of_use'),
        # USER URLS
        path('first-login/', users.first_login_page, name='first_login'),
        path('first-login-validate/', users.first_login_validate, name='first_login_validate'),
        path('force-password-change/', users.force_password_change, name='force_password_change'),
        path('login/', auth_views.LoginView.as_view(template_name='user/users/login.html'), name='login'),
        path('password-change/', auth_views.PasswordChangeView.as_view(template_name='user/users/password_change.html'), name='password_change'),
        path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/users/password_reset.html'), name='password_reset'),
        path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/users/password_reset_done.html'), name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/users/password_reset_confirm.html'), name='password_reset_confirm'),
        path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/users/password_reset_complete.html'), name='password_reset_complete'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('profile/', users.profile, name='profile'),
        path('profile/update/', users.profile_update, name='profile_update'),
        path('social-links/', users.social_links, name='social_links'),
        path('favorite_video/<int:pk>/', users.favorite_video, name='favorite_video'),
        path('favorite-videos/', users.favorite_videos, name='favorite_videos'),
        # USER LIST URLS
        path('users/', include([
            path('instructors/', instructors.instructor_list, name='instructors_list'),
        ])),
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
