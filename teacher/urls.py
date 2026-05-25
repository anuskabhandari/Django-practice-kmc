from django.urls import path

from teacher.views import TeacherCreate, TeacherUpdate, teacher_delete, teacher_list , create_teacher, teacher_update , TeacherView

urlpatterns=[
    path('teacher',teacher_list, name="teacher"),
    path('teacher-create',create_teacher, name="teacher-create"),
    path('teacher_update/<int:id>', teacher_update, name="update"),
    path('teacher_delete/<int:id>', teacher_delete, name="delete"),
    path('teacher-class-list',TeacherView.as_view(), name="teacher-class"),
    path('teacher-class-create',TeacherCreate.as_view(), name="teacher-class-create"),
    path('teacher-class-update/<int:pk>',TeacherUpdate.as_view(), name="teacher-class-update"),
]
