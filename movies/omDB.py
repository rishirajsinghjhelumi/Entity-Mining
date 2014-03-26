#!/usr/bin/env python

import omdb

def getMovies(query):

	movies = omdb.search(query)

	return movies
