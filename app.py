#!/usr/bin/env python

from movies import tmDB
from movies import imDB
from movies import omDB
from movies import rt
from tmdb3 import Person, Movie, List, Studio

def main():

	# print tmDB.getMovies('pirates of the caribbean')
	# print imDB.getMovies('goonies')
	# print omDB.getMovies('goonies')
	# print rt.getMovies('pirates', limit = 10)

	# print tmDB.getNowPlayingMovies(limit = 20)
	# print tmDB.getMovieInfo(Movie(9340))
	print rt.getIMDBMovieInfo(1291150)

if __name__ == '__main__':
	main()