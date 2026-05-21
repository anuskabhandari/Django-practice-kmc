## yesko name j rakhda nii hunxa like route.py
from django.urls import path

from home.views import home, home__json, landing_page, student_create, student_create2, student_list, student_update, student_delete


urlpatterns = [
    path('', home, name = "home"),# name ralhyo vne reverse mapping hunxa but tyo browser ma kam gardaina only in code
    path('json/', home__json, name = "json-data"),
    path('home_page',landing_page, name="page"),
    path('student_list', student_list,name="student"),
    path('student_create', student_create,name="create"),
    path('student_create2', student_create2,name="create2"),
    path('student_update/<int:id>', student_update, name="update"),
    path('student_delete/<int:id>', student_delete, name="delete"),

]
# first ma ko path ma empty rakhe beacuse from the core project home chalda diretly tyo khulxa not need home/home
