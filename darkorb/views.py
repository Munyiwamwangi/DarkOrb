from django.shortcuts import render
import requests
from .models import Movie
# Create your views here.

def home(request):

	url = 'https://api.themoviedb.org/3/movie/popular?api_key=0e53893601f4571b5f08dafad21f6272'
	r = requests.get(url.format()).json()
	movie_list = r['results']
	print(movie_list)
	movie_results = []
	for movie_item in movie_list:
		id = movie_item.get('id')
		title = movie_item.get('original_title')
		overview = movie_item.get('overview')
		image = movie_item.get('poster_path')
		rating = movie_item.get('vote_average')
		vote_count = movie_item.get('vote_count'),
		age = movie_item.get('genre_ids[3]')

		if image:
			movie_object = Movie(id,title,overview,image,rating,vote_count,age)
			movie_results.append(movie_object)
			
	return render(request, "home.html", {"allmovies": movie_results})