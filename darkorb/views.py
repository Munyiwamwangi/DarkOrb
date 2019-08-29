from django.shortcuts import render
import requests

# Create your views here.
def home(requests):
	url = 'https://api.themoviedb.org/3/movie/550?api_key=0e53893601f4571b5f08dafad21f6272'
	response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=0e53893601f4571b5f08dafad21f6272')
	moviedata = response.json()
	return render(request, 'home.html', {
		'id': moviedata['id'],
		'title': moviedata['title'],
		# 'genres': moviedata['genres['name']'],
		'overview': moviedata ['overview']
		'release_date': moviedata['release_date'],
        'poster_path': moviedata['poster_path'],
        'vote_count': moviedata['vote_count'],

		})