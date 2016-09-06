# Flix

### Description
This project was designed to introduce the process of making a Django project and the front-end aspect of a final project as well as reinforce the idea of working with a database. Specifically, this project involves models including approx. 4,000 movies, at least 6,000 users, approx. 1,000,000 ratings, and 18 genres. The application allows users to register, login, and logout. Logged in users can rate movies they have not seen before and update ratings for movies they have already rated.  Users may also search through the entire database of movies if they do not see a desired movie in their personalized recommendation list on their page.  A trailer is available on each movie's detail page.   


## How to run
* ```pip install -r requirements.txt```
* Make sure you have a PostgreSQL database named ```movielens```
* ```python manage.py migrate``` (This will take several minutes due to the size of the files.)
* Create a file named ```secrets.py``` in your project folder with your specific DATABASES information and your SECRET_KEY


## Included Files
  - movielens Django project: our Django project
  - flix Django app: contains the models for Rater, Rating, Movie and Genre
  - data folder: the MovieLens 1M dataset
  - requirements.txt: required installs

## Notes
  - As of this moment, you need to create your own youtube search function utilizing the YouTube Data API... we intend to include this soon.  You will, however, still need a Google API Key
