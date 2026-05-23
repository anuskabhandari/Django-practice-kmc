from django.shortcuts import render

from movie.models import Movie

# Create your views here.
def movie_list(request):
    movie = Movie.objects.all()
    context ={
        "movie" : movie
    }
    return render(request,'movie/index.html', context)
