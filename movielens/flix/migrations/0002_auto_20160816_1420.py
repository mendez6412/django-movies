# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 19:20
from __future__ import unicode_literals

from django.db import migrations
import datetime
import csv


def parse_data(apps, schema_editor):
    Movie = apps.get_model('flix', 'Movie')
    Rater = apps.get_model('flix', 'Rater')
    Rating = apps.get_model('flix', 'Rating')

    movie_dict = {}
    rater_dict = {}

    with open('../data/movies.dat', encoding='latin_1') as movies:
        reader = csv.reader(movies, delimiter='+')
        for row in reader:
            temp = Movie(id=int(row[0]), title=row[1], genre=row[2])
            movie_dict[temp.id] = temp
            temp.save()

    with open('../data/users.dat') as raters:
        reader = csv.reader(raters, delimiter='+')
        for row in reader:
            temp = Rater(id=int(row[0]), gender=row[1], age=int(row[2]), occupation=int(row[3]), zipcode=row[4])
            rater_dict[temp.id] = temp
            temp.save()

    with open('../data/ratings.dat') as ratings:
        reader = csv.reader(ratings, delimiter='+')
        for row in reader:
            dt = datetime.datetime.fromtimestamp(float(row[3]))
            # temp = Rating(rater=rater_dict[int(row[0])], movie=movie_dict[int(row[1])], rating=int(row[2]), timestamp=dt)
            # Save below should be siginificantly faster, it wasn't
            temp = Rating(rater_id=int(row[0]), movie_id=int(row[1]), rating=int(row[2]), timestamp=dt)
            temp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('flix', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(parse_data)
    ]
