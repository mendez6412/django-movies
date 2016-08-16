from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^movie/([0-9]+)/$', views.movie, name='movie'),
    url(r'^rater/([0-9]+)/$', views.rater, name='rater'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='logout'),
    url(r'^register/$', views.register, name='register')
    ]
