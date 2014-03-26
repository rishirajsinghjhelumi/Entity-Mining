#!/usr/bin/env python

import imdb

db = imdb.IMDb()

def getMovies(query):

	movies = db.search_movie(query)

	return movies

