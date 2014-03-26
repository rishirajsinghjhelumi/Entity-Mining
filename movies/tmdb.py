#!/usr/bin/env python

from config import apiKeys

from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import set_locale
from tmdb3 import searchMovie

set_key(apiKeys['tmdb'])
set_cache('null')
set_locale('en', 'gb')

# cast, crew, getSimilar, Lists
# mostpopular, nowplaying
# favorites, ratedmovies

def getMovieInfoAsJSON(movie):

	movieInfo = {}

	# Movie titles
	movieInfo['title']['main'] = movie.title
	movieInfo['title']['originale_title'] = movie.originaletitle
	movieInfo['title']['alternative_titles'] = {}
	for movieTitles in movie.alternate_titles:
		movieInfo['title']['alternative_titles'][movieTitles.country] = movieTitles.title

	# Movie Adult
	movieInfo['is_adult'] = movie.adult

	# Movie Budget
	movieInfo['budget'] = movie.budget

	# Movie Homepage
	movieInfo['homepage'] = movie.homepage

	# Movie TMDB ID
	movieInfo['id_tmdb'] = movie.id

	# Movie IMDB ID
	movieInfo['id_imdb'] = movie.imdb

	# Movie Overview
	movieInfo['overview'] = movie.overview

	# Movie Popularity
	movieInfo['popularity'] = movie.popularity

	# Movie Revenue
	movieInfo['revenue'] = movie.revenue

	# Movie Release Date
	movieInfo['release_date']['main'] = movie.releasedate.strftime('%s')
	movieInfo['release_date']['countries'] = {}
	for country in movies.releases:
		movieInfo['release_date']['countries'][country] = movie.releases[country].releasedate.strftime('%s')


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

	# Countries
	movieInfo['countries'] = []
	for country in movie.countries:
		movieInfo['countries'].append({'code' : country.code, 'name' : country.name})

	# Movie Genres
	movieInfo['genres'] = []
	for genre in movie.genres:
		movieInfo['genres'].append({'id' : genre.id, 'name' : genre.name })

	# Movie Keywords
	movieInfo['keywords'] = []
	for keyword in movie.keywords:
		movieInfo['keywords'].append({'id' : keyword.id, 'name' : keyword.name })

	# Languages
	movieInfo['languages'] = []
	for language in movie.languages:
		movieInfo['languages'].append({'code' : language.code, 'name' : language.name})

	return movieInfo

def getMovies(query):

	movies = searchMovie(query)
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMovieInfoAsJSON(movie))

	return {'query' : query, 'domain' : 'tmdb', 'movies' : movies}

