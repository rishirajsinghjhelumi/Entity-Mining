#!/usr/bin/env python

from movies.tmdb import getMovies

def main():

	print getMovies('goonies')

if __name__ == '__main__':
	main()