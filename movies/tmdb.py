#!/usr/bin/env python

from config import apiKeys

from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import set_locale
from tmdb3 import searchMovie

set_key(apiKeys['tmdb'])
set_cache('null')
set_locale('en', 'gb')

def getMovieInfoAsJSON(movie):

	movieInfo = {}
	# Movie Adult
	movieInfo['is_adult'] = movie.adult

	# Movie Budget
	movieInfo['budget'] = movie.budget

	# Movie Title is Different Languages
	movieInfo['alternative_titles'] = {}
	for movieTitles in movie.alternate_titles:
		movieInfo['alternative_titles'][movieTitles.country] = movieTitles.title

	# Apple Trailers
	movieInfo['apple_trailers'] = {}
	for appleTrailer in movie.apple_trailers:
		movieInfo['apple_trailers']['name'] = appleTrailer.name
		movieInfo['apple_trailers']['trailer'] = {}
		for size in appleTrailer.sizes():
			movieInfo['apple_trailers']['trailer'][size] = appleTrailer.geturl(size)

	# Images
	movieInfo['images'] = []
	movieInfo['images'].append(movie.backdrop.geturl())
	for image in movie.backdrops:
		movieInfo['images'].append(image.geturl())

	# Posters
	movieInfo['posters'] = []
	movieInfo['posters'].append(movie.poster.geturl())
	for poster in movie.posters:
		movieInfo['posters'].append(poster.geturl())

	return movieInfo

def getMovies(query):

	movies = searchMovie(query)
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMovieInfoAsJSON(movie))

	return {'query' : query, 'movies' : movies}
