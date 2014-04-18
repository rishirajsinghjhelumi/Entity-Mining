from app import app
from flask import request
from flask import jsonify

from movies import tmDB
from movies import imDB
from movies import omDB
from movies import rt
from tmdb3 import Person, Movie, List, Studio

from util import ResponseJSON

@app.route("/movies/now_playing/<int:limit>/<int:offset>",methods=['GET'])
def moviesNowPlaying(limit, offset):

	return ResponseJSON(tmDB.getNowPlayingMovies(limit = limit, offset = offset))

@app.route("/movies/most_popular/<int:limit>/<int:offset>",methods=['GET'])
def moviesMostPopular(limit, offset):

	return ResponseJSON(tmDB.getMostPopularMovies(limit = limit, offset = offset))

@app.route("/movies/top_rated/<int:limit>/<int:offset>",methods=['GET'])
def moviesTopRated(limit, offset):

	return ResponseJSON(tmDB.getTopRatedMovies(limit = limit, offset = offset))

@app.route("/movies/upcoming/<int:limit>/<int:offset>",methods=['GET'])
def moviesUpcoming(limit, offset):

	return ResponseJSON(tmDB.getUpcomingMovies(limit = limit, offset = offset))

@app.route("/movies/top_box_office/<int:limit>",methods=['GET'])
def moviesTopBoxOffice(limit):

	return ResponseJSON(rt.getTopBoxOfficeMovies(limit = limit))

@app.route("/movies/opening_this_week/<int:limit>",methods=['GET'])
def moviesOpeningThisWeek(limit):

	return ResponseJSON(rt.getThisWeekOpeningMovies(limit = limit))

@ResponseJSON
@app.route("/movies/in_theatre/<int:limit>/<int:page>",methods=['GET'])
def moviesInTheatre(limit, page):

	return ResponseJSON(rt.getInTheatreMovies(limit = limit, page = page))

@app.route("/dvd/top_rental/<int:limit>",methods=['GET'])
def dvdsTopRental(limit):

	return ResponseJSON(rt.getTopRentalDVDs(limit = limit))

@app.route("/dvd/current_released/<int:limit>/<int:page>",methods=['GET'])
def dvdsCurrentReleased(limit, page):

	return ResponseJSON(rt.getCurrentReleasedDVDs(limit = limit, page = page))

@app.route("/dvd/new_released/<int:limit>/<int:page>",methods=['GET'])
def dvdsNewReleased(limit, page):

	return ResponseJSON(rt.getNewReleasedDVDs(limit = limit, page = page))

@app.route("/dvd/upcoming/<int:limit>/<int:page>",methods=['GET'])
def dvdsUpcoming(limit, page):

	return ResponseJSON(rt.getUpcomingDVDs(limit = limit, page = page))

@app.route("/movies/tmdb/search/<query>",methods=['GET'])
def moviesTMDBSearch(query):

	return ResponseJSON(tmDB.getMovies(query))

@app.route("/movies/tmdb/info/<int:movie_id>",methods=['GET'])
def movieTMDBQuery(movie_id):

	return ResponseJSON(tmDB.getMovieInfo(Movie(movie_id)))

@app.route("/movies/rt/search/<query>/<int:limit>/<int:page>",methods=['GET'])
def moviesRTSearch(query, limit, page):

	return ResponseJSON(rt.getMovies(query, limit = limit, page = page))

@app.route("/movies/rt/info/<int:movie_id>",methods=['GET'])
def movieRTQuery(movie_id):

	return ResponseJSON(rt.getMovieInfo(movie_id))