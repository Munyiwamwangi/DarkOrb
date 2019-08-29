from django.shortcuts import render
import requests

# Create your views here.
def home(requests):
	response = requests.get(https://api.themoviedb.org/3/movie/550?api_key=0e53893601f4571b5f08dafad21f6272)
	moviedata = respnse.json()
	return render(reqiest, 'home.html', {
		'id': moviedata('movie_id'),
		'overview': geodata ['movie_overview']
		'poster': geodata['movie_poster'],
        'title': geodata['movie_title'],
        'vote_count': geodata['latitude'],
        'poster_path': geodata['movie_poster_path']
        'vote_count': geodata['vote_count']

		})