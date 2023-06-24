from django.urls import path, include
from .views import main, students

urlpatterns = [
    path('', include([
        path('', main.dashboard, name='admin_dashboard'),
        path('general-settings/', main.general_settings, name='admin_general_settings'),
        path('students/', include([
            path('', students.students_page, name='admin_students_list'),
            path('create/', students.student_create, name='admin_students_create'),
            path('update/<int:pk>/', students.student_update, name='admin_students_update'),
            path('delete/<int:pk>/', students.student_delete, name='admin_students_delete'),
        ])),
    ]))
]
