from app import app
from flask import request
from flask import jsonify

from movies import tmDB
from movies import imDB
from movies import omDB
from movies import rt
from tmdb3 import Person, Movie, List, Studio

@app.route("/movies/now_playing/<int:limit>/<int:offset>",methods=['GET'])
def moviesNowPlaying(limit, offset):

	return tmDB.getNowPlayingMovies(limit = limit, offset = offset)

@app.route("/movies/most_popular/<int:limit>/<int:offset>",methods=['GET'])
def moviesMostPopular(limit, offset):

	return tmDB.getMostPopularMovies(limit = limit, offset = offset)

@app.route("/movies/top_rated/<int:limit>/<int:offset>",methods=['GET'])
def moviesTopRated(limit, offset):

	return tmDB.getTopRatedMovies(limit = limit, offset = offset)

@app.route("/movies/upcoming/<int:limit>/<int:offset>",methods=['GET'])
def moviesUpcoming(limit, offset):

	return tmDB.getUpcomingMovies(limit = limit, offset = offset)