from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater, Rating
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import connection


def index(request):
    # look @ .values_list
    # django debug toolbar, extensions, ODO
    """ SQL Magic, current clock @ ~600ms... so not quite Google time """
    # T: ASK ME TO EXPLAIN
    cur = connection.cursor()
    cur.execute('SELECT movie_id, AVG(rating) as a FROM flix_rating GROUP BY movie_id HAVING COUNT (movie_id) > 20ORDER BY a DESC;')
    top20 = cur.fetchmany(20)
    temp = []
    for item in top20:
       movie = Movie.objects.get(id=item[0])
       temp.append((movie.id, movie.title, round(item[1], 2)))
    context = {'top20': temp}

    # Let's talk about why .aggregate won't work well here
    # average = Movie.objects.aggergate(Avg('rating__rating'))
    # movie = Movie.objects.all()
    # context = {
    #     'average': average,
    #     'movie': movie,
    # }
    return render(request, 'flix/index.html', context)
    # return HttpResponse('you are at the index')


def movie(request, movie_id):
    # someone explain get_or_404 to me(Tommy) tomorrow
    # someone explain why you don't need to int(movie_id), as pk is an int
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = Rating.objects.filter(movie_id=movie.id)
    avg_rating = movie.rating_set.aggergate(Avg('rating'))
    context = {
        'movie': movie,
        'ratings': ratings,
        'avg_rating': avg_rating
    }
    return render(request, 'flix/movie.html', context)


def rater(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = Rating.objects.filter(rater_id=rater_id)
    movies_rated = []
    for movie in ratings:
        title = Movie.objects.get(id=movie.movie_id)
        movies_rated.append((title, movie.movie_id, movie.rating))
    context = {
        'rater': rater,
        'movies_rated': movies_rated
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
            # T: good question, probably their own profile page or the index
            return render(request, "flix/rater/{}".format(user.id), {})
    else:
        # return render()  # where should we send them here? help
        return render(request, "flix/login.html", {})
        # T: good question, probably the index


def signout(request):
    logout(request)
    return render(request, 'flix/logout.html')
    # Just FYI, flix/logout.html should be a "SUCCESS" page
    # Meaning something like "Yes, you logged out."


def register(request):
    pass
    # Here we need 2 forms, a USER CREATION FORM and a RATER CREATION FORM
    # I'll leave this for tomorrow, but it's important and we should all
    # look at this.  -t
