#!/usr/bin/env python

from config import apiKeys

from util import jsonify

from rottentomatoes import RT

rt = RT(apiKeys['rotten_tomatoes'])
_ROTTEN_TOMATOES_LIMIT = 50

@jsonify
def getMovieInfo(movieId):

	movieInfo = rt.info(movieId)
	movieInfo.update(rt.info(movieId, 'cast'))
	movieInfo.update(rt.info(movieId, 'reviews'))
	movieInfo.update(rt.info(movieId, 'similar'))
	movieInfo.update(rt.info(movieId, 'clips'))

	return movieInfo

@jsonify
def getMovies(query, limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.search(query, page_limit = limit, page = page)

	return {'query' : query, 'domain' : 'rotten_tomatoes', 'movies' : movies}

@jsonify
def getTopBoxOfficeMovies(limit = 10):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.movies('box_office', page_limit = limit)

	return {'top_box_office' : movies}

@jsonify
def getThisWeekOpeningMovies(limit = 10):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.movies('opening', page_limit = limit)

	return {'opening' : movies}

@jsonify
def getInTheatreMovies(limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.movies('in_theaters', page_limit = limit, page = page)

	return {'in_theaters' : movies}

@jsonify
def getUpcomingMovies(limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.movies('upcoming', page_limit = limit, page = page)

	return {'upcoming' : movies}

@jsonify
def getTopRentalDVDs(limit = 10):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.dvds('top_rentals', page_limit = limit)

	return {'top_rentals' : movies}

@jsonify
def getCurrentReleasedDVDs(limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.dvds('current_releases', page_limit = limit, page = page)

	return {'current_releases' : movies}

@jsonify
def getNewReleasedDVDs(limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.dvds('new_releases', page_limit = limit, page = page)

	return {'new_releases' : movies}

@jsonify
def getUpcomingDVDs(limit = 10, page = 1):

	limit = min(limit, _ROTTEN_TOMATOES_LIMIT)
	movies = rt.dvds('upcoming', page_limit = limit, page = page)

	return {'upcoming' : movies}