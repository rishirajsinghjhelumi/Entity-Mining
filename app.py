#!/usr/bin/env python

from movies import tmdb
from movies import imDB

def main():

	print tmdb.getMovies('goonies')
	print imDB.getMovies('inception')

if __name__ == '__main__':
	main()