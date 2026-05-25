from django.urls import path

from teacher.views import teacher_delete, teacher_list , create_teacher, teacher_update

urlpatterns=[
    path('teacher',teacher_list, name="teacher"),
    path('teacher-create',create_teacher, name="teacher-create"),
     path('teacher_update/<int:id>', teacher_update, name="update"),
    path('teacher_delete/<int:id>', teacher_delete, name="delete"),
]
