#!/usr/bin/env python

from movies import tmDB
from movies import imDB
from movies import omDB

def main():

	print tmDB.getMovies('goonies')
	print imDB.getMovies('goonies')
	print omDB.getMovies('goonies')

if __name__ == '__main__':
	main()