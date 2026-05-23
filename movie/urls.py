from django.urls import path

from movie.views import movie_list


urlpatterns=[
    path('movie',movie_list, name="movie"),
]