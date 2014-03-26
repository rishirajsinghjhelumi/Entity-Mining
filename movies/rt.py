#!/usr/bin/env python

from rottentomatoes import RT
from config import apiKeys

rt = RT(apiKeys['rotten_tomatoes'])

def getMovies(query):

	movies = rt.search(query)

	return movies
