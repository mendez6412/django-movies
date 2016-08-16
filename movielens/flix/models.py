from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=240)
    genre = models.CharField(max_length=240)

    def __str__(self):
        return self.title


class Raters(models.Model):
    OCCUPATIONS = (
        (0, "other"), (1, "academic/educator"),
        (2, "artist"), (3, "clerical/admin"),
        (4, "college/grad student"), (5, "customer service"),
        (6, "doctor/health care"), (7, "executive/managerial"),
        (8, "farmer"), (9, "homemaker"), (10, "K-12 student"),
        (11, "lawyer"), (12, "programmer"), (13, "retired"),
        (14, "sales/marketing"), (15, "scientist"),
        (16, "self-employed"), (17, "technician/engineer"),
        (18, "tradesman/craftsman"), (19, "unemployed"), (20, "writer"))

    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.IntegerField(choices=OCCUPATIONS)
    zipcode = models.CharField(max_length=20)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)


class Rating(models.Model):
    rater = models.ForeignKey('Rater', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    timestamp = models.DateTimeField(auto_now=True)
