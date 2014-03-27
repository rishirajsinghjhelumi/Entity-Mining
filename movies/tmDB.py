#!/usr/bin/env python

from config import apiKeys

from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import set_locale
from tmdb3 import searchMovie, searchPerson, searchSeries
from tmdb3 import Movie, Person, Collection, Studio, Series, Season, Episode

set_key(apiKeys['tmdb'])
set_cache('null')
set_locale('en', 'gb')

def getPersonInfo(person):
	
	personInfo = {}

	personInfo['name'] = person.name
	personInfo['adult'] = person.adult
	personInfo['biography'] = person.biography

	personInfo['aliases'] = []
	for alias in person.aliases:
		personInfo['aliases'].append(alias)

	personInfo['birthplace'] = person.birthplace
	personInfo['birthdate'] = person.dayofbirth if person.dayofbirth is not None else None
	personInfo['deathdate'] = person.dayofdeath if person.dayofdeath is not None else None

	personInfo['homepage'] = person.homepage
	personInfo['id_tmdb'] = person.id

	personInfo['images'] = []
	if person.profile is not None:
		personInfo['images'].append(person.profile.geturl())
	for profile in person.profiles:
		personInfo['images'].append(profile.geturl())

	# Reverse Roles
	personInfo['roles'] = []
	for movie in person.roles:
		role = {}
		role['character'] = movie.character
		role['movie'] = getMinimalistMovieInfo(movie)
		personInfo['roles'].append(role)

	# Reverse Crew
	personInfo['crew'] = []
	for movie in person.crew:
		crew = {}
		crew['job'] = movie.job
		crew['department'] = movie.department
		crew['movie'] = getMinimalistMovieInfo(movie)
		personInfo['crew'].append(crew)

	return personInfo


def getStudioInfo(studio):
	pass

def getMovieListInfo(movieList):
	pass

def getMovieInfo(movie):

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
	movieInfo['adult'] = movie.adult

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
	movieInfo['release_date']['main'] = movie.releasedate
	movieInfo['release_date']['countries'] = {}
	for country in movie.releases:
		movieInfo['release_date']['countries'][country] = movie.releases[country].releasedate

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

	# Available Translations
	movieInfo['translations'] = []
	for translation in movie.translations:
		movieInfo['translations'].append({'language' : translation.language, 'name' : translation.englishname})

	return movieInfo

def getMinimalistMovieInfo(movie):

	movieInfo = {}
	movieInfo['id_tmdb'] = movie.id
	movieInfo['title'] = movie.title
	movieInfo['release_date'] = movie.releasedate if movie.releasedate is not None else None
	movieInfo['image'] = movie.poster.geturl() if movie.poster is not None else None

	return movieInfo

def getMinimalistPersonInfo(person):

	personInfo = {}
	personInfo['id_tmdb'] = person.id
	personInfo['name'] = person.name
	personInfo['biography'] = person.biography
	personInfo['image'] = person.profile.geturl() if person.profile is not None else None

	return personInfo

def getMovies(query):

	movies = searchMovie(query)
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'query' : query, 'domain' : 'tmdb', 'movies' : movieInfo}

def getMostPopularMovies(limit = 10, offset = 0):

	movies = Movie.mostpopular()[offset : offset + limit]
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'most_popular' : movieInfo}


def getNowPlayingMovies(limit = 10, offset = 0):

	movies = Movie.nowplaying()[offset : offset + limit]
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'now_playing' : movieInfo}

def getTopRatedMovies(limit = 10, offset = 0):

	movies = Movie.toprated()[offset : offset + limit]
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'top_rated' : movieInfo}


def getUpcomingMovies(limit = 10, offset = 0):

	movies = Movie.upcoming()[offset : offset + limit]
	movieInfo = []
	for movie in movies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'upcoming' : movieInfo}

def getSimilarMovies(movie, limit = 10, offset = 0):

	similarMovies = movie.similar[offset : offset + limit]
	moviesInfo = []
	for movie in similarMovies:
		movieInfo.append(getMinimalistMovieInfo(movie))

	return {'similar' : movieInfo}
