from django.urls import path

from teacher.views import teacher_list , create_teacher

urlpatterns=[
    path('teacher',teacher_list, name="teacher"),
    path('teacher-create',create_teacher, name="teacher-create")
]
