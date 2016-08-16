from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=240)
    genre = models.CharField(max_length=240)

    def __str__(self):
        return self.title

class Raters(models.Model):
    occupations = [
        (0, "other")
        (1, "academic/educator"
        (2, "artist"
        (3, "clerical/admin"
        (4, "college/grad student"
        (5, "customer service"
        (6, "doctor/health care"
        (7, "executive/managerial"
        (8, "farmer"
        (9, "homemaker"
        (10, "K-12 student"
        (11, "lawyer"
        (12, "programmer"
        (13, "retired"
        (14, "sales/marketing"
        (15, "scientist"
        (16, "self-employed"
        (17, "technician/engineer"
        (18, "tradesman/craftsman"
        (19, "unemployed"
        (20, "writer"
    ]


    gender = model.CharField(max_length=10)
    age = model.IntegerField()
    occupation = model.IntegerField()
    zipcode = model.

class Rating(models.Model):
