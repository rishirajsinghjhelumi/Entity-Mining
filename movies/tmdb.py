#!/usr/bin/env python

from config import apiKeys

from lib.tmdb3 import set_key
from lib.tmdb3 import set_cache
from lib.tmdb3 import set_locale
from lib.tmdb3 import searchMovie

set_key(apiKeys['tmdb'])
set_cache('null')
set_locale('en', 'gb')

# TODO (WILL BE LINKS) : cast, crew, smilar, lists, studios, translations
# MAIN PAGE CONTENT : mostpopular, nowplaying, toprated, upcoming
# NOT REQUIRED : favorites, ratedmovies, setFavorite, setRating, setWatchlist, watchlist

def _getMovieInfoAsJSON(movie):

	movieInfo = {}

	# Movie titles
	movieInfo['title'] = {}
	movieInfo['title']['main'] = movie.title
	movieInfo['title']['originale_title'] = movie.originaltitle
	movieInfo['title']['alternate_titles'] = []
	for movieTitle in movie.alternate_titles:
		title = {}
		title['country'] = movieTitle.country
		title['title'] = movieTitle.title
		movieInfo['title']['alternate_titles'].append(title)

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

	# Movie Runtime
	movieInfo['runtime'] = movie.runtime

	# Movie Tagline
	movieInfo['tagline'] = movie.tagline

	# Movie votes
	movieInfo['votes'] = movie.votes

	# Movie Release Date
	movieInfo['release_date'] = {}
	movieInfo['release_date']['main'] = movie.releasedate.strftime('%s')
	movieInfo['release_date']['countries'] = {}
	for country in movie.releases:
		movieInfo['release_date']['countries'][country] = movie.releases[country].releasedate.strftime('%s')

	# Apple Trailers
	movieInfo['trailers'] = {}
	movieInfo['trailers']['apple'] = []
	for appleTrailer in movie.apple_trailers:
		trailer = {}
		trailer['name'] = appleTrailer.name
		trailer['trailers'] = appleTrailer.geturl()
		movieInfo['trailers']['apple'].append(trailer)

	# Youtube Trailers
	movieInfo['trailers']['youtube'] = []
	for youtubeTrailer in movie.youtube_trailers:
		trailer = {}
		trailer['name'] = youtubeTrailer.name
		trailer['trailers'] = youtubeTrailer.geturl()
		movieInfo['trailers']['youtube'].append(trailer)

	# Images
	movieInfo['images'] = []
	if movie.backdrop is not None:
		movieInfo['images'].append(movie.backdrop.geturl())
	for image in movie.backdrops:
		movieInfo['images'].append(image.geturl())

	# Posters
	movieInfo['posters'] = []
	if movie.poster is not None:
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
		movieInfo.append(_getMovieInfoAsJSON(movie))

	return {'query' : query, 'domain' : 'tmdb', 'movies' : movieInfo}

