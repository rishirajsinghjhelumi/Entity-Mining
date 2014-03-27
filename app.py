#!/usr/bin/env python

from movies import tmDB
from movies import imDB
from movies import omDB
from movies import rt

def main():

	# print tmDB.getMovies('goonies')
	# print imDB.getMovies('goonies')
	# print omDB.getMovies('goonies')
	# print rt.getMovies('goonies')

	tmDB.getNowPlayingMovies()

if __name__ == '__main__':
	main()