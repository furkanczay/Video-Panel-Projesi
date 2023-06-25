from django.urls import path, include
from .views import main, students, instructors, groups

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
    ]))
]
