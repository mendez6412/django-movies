from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Movie, Rater, Rating
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from .moresecrets import youtube_search
from .forms import RaterForm, RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse


def index(request):
    # look @ .values_list
    # django debug toolbar, extensions, ODO
    """ SQL Magic, current clock @ ~600ms... so not quite Google time """
    cur = connection.cursor()
    cur.execute('SELECT movie_id, AVG(rating) as a FROM flix_rating GROUP BY movie_id HAVING COUNT (movie_id) > 20ORDER BY a DESC;')
    top20 = cur.fetchmany(20)
    temp = []
    for item in top20:
        movie = Movie.objects.get(id=item[0])
        temp.append((movie.id, movie.title, round(item[1], 2)))
    context = {'top20': temp}
    return render(request, 'flix/index.html', context)


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = Rating.objects.filter(movie_id=movie.id)
    avg_rating = round(movie.rating_set.aggregate(Avg('rating'))['rating__avg'], 2)
    trailer = youtube_search("{} trailer".format(movie.title))[0]
    context = {
        'movie': movie,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'trailer': trailer
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
            return HttpResponseRedirect(reverse(rater, args=[request.user.id]))
    else:
        return render(request, "flix/login.html", {})


def signout(request):
    logout(request)
    return render(request, 'flix/logout.html')


def register(request):
    if request.method == 'POST':
        rater_form = RaterForm(request.POST, prefix='rater')
        user_form = UserCreationForm(request.POST, prefix='user')
        if rater_form.is_valid() * user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            rater = rater_form.save(commit=False)
            rater.user_id = user.id
            rater.id = user.id
            rater.save()
            return HttpResponseRedirect('/')
    else:
        rater_form = RaterForm(prefix='rater')
        user_form = UserCreationForm(prefix='user')
        context = {'raterform': rater_form, 'userform': user_form}
        return render(request, 'flix/register.html', context)


def get_new_rating(request, movie_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            rating_form = RatingForm(request.POST, prefix='rating')
            if rating_form.is_valid():
                new_rating = rating_form.save(commit=False)
                new_rating.rater_id = request.user.id
                new_rating.movie_id = movie_id
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/register/')


# temp = Rater.objects.get(user_id=request.user.id).id
