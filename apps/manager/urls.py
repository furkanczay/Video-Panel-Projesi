from django.urls import path, include
from .views import main, students, instructors, groups, courses, videos

urlpatterns = [
    path('', include([
        path('', main.dashboard, name='admin_dashboard'),
        path('general-settings/', main.general_settings, name='admin_general_settings'),
        # STUDENTS URLS
        path('students/', include([
            path('', students.students_page, name='admin_students_list'),
            path('create/', students.student_create, name='admin_students_create'),
            path('update/<int:pk>/', students.student_update, name='admin_students_update'),
            path('delete/<int:pk>/', students.student_delete, name='admin_students_delete'),
            path('<int:pk>/password/', main.user_update_password, name='admin_students_update_password'),
        ])),
        # INSTRUCTORS URLS
        path('instructors/', include([
            path('', instructors.instructors_page, name='admin_instructors_list'),
            path('create/', instructors.instructor_create, name='admin_instructors_create'),
            path('update/<int:pk>/', instructors.instructor_update, name='admin_instructors_update'),
            path('delete/<int:pk>/', instructors.instructor_delete, name='admin_instructors_delete'),
            path('<int:pk>/password/', main.user_update_password, name='admin_instructors_update_password'),
        ])),
        # GROUPS URLS
        path('groups/', include([
            path('', groups.groups_page, name='admin_groups_page'),
            path('create/', groups.group_create, name='admin_groups_create'),
            path('update/<int:pk>/', groups.group_update, name='admin_groups_update'),
            path('delete/<int:pk>/', groups.group_delete, name='admin_groups_delete'),
        ])),
        # COURSE CATEGORIES URLS
        path('course-categories/', include([
            path('', courses.course_categories_page, name='admin_course_categories_page'),
            path('create', courses.course_category_create, name='admin_course_categories_create'),
            path('update/<int:pk>/', courses.course_category_update, name='admin_course_categories_update'),
            path('delete/<int:pk>/', courses.course_category_delete, name='admin_course_categories_delete'),
        ])),
        # COURSES URLS
        path('courses/', include([
            path('', courses.courses_page, name='admin_courses_page'),
            path('create/', courses.course_create, name='admin_courses_create'),
            path('update/<int:pk>/', courses.course_update, name='admin_courses_update'),
            path('delete/<int:pk>/', courses.course_delete, name='admin_courses_delete'),
        ])),
        # CLASSROOMS URLS
        path('classrooms/', include([
            path('', courses.classrooms_page, name='admin_classrooms_page'),
            path('create/', courses.classrooms_create, name='admin_classrooms_create'),
            path('update/<int:pk>/', courses.classroom_update, name='admin_classrooms_update'),
            path('delete/<int:pk>/', courses.classroom_delete, name='admin_classrooms_delete'),
        ])),
        # VIDEOS URLS
        path('videos/', include([
            path('', videos.videos_page, name='admin_videos_page'),
            path('create/', videos.video_create, name='admin_videos_create'),
            path('update/<int:pk>/', courses.classroom_update, name='admin_videos_update'),
            path('delete/<int:pk>/', courses.classroom_delete, name='admin_videos_delete'),
        ])),
    ]))
]
