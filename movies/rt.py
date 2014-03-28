#!/usr/bin/env python

from config import apiKeys

from util import jsonify

from rottentomatoes import RT

rt = RT(apiKeys['rotten_tomatoes'])

@jsonify
def getMovies(query, limit = 10, page = 1):

	limit = min(limit, 50)
	movies = rt.search(query, page_limit = limit, page = page)

	return {'query' : query, 'domain' : 'rotten_tomatoes', 'movies' : movies}

@jsonify
def getTopBoxOfficeMovies(limit = 10):

	limit = min(limit, 50)
	movies = rt.movies('box_office', page_limit = limit)

	return {'top_box_office' : movies}

@jsonify
def getThisWeekOpeningMovies(limit = 10):

	limit = min(limit, 50)
	movies = rt.movies('opening', page_limit = limit)

	return {'opening' : movies}

@jsonify
def getInTheatreMovies(limit = 10, page = 1):

	limit = min(limit, 50)
	movies = rt.movies('in_theaters', page_limit = limit, page = page)

	return {'in_theaters' : movies}

@jsonify
def getUpcomingMovies(limit = 10, page = 1):

	limit = min(limit, 50)
	movies = rt.movies('upcoming', page_limit = limit, page = page)

	return {'upcoming' : movies}
