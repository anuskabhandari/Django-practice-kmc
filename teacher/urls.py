from django.urls import path

from teacher.views import teacher_list

urlpatterns=[
    path('teacher',teacher_list, name="teacher")
]
