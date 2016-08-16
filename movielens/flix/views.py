from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater, Rating
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    # average = Movie.objects.aggergate(Avg('rating__rating'))
    # movie = Movie.objects.all()
    # context = {
    #     'average': average,
    #     'movie': movie,
    # }
    # return render(request, 'flix/index.html', context)
    return HttpResponse('your at the index')


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'flix/movie.html', context)


def rater(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    context = {
        'rater': rater,
    }
    return render(request, 'flix/rater.html', context)


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Where should we sent the user?
    else:
        return render()  # where should we send them here? help


def signout(request):
    logout(request)
    return render(request, 'flix/logout.html')


def register(request):
    pass
