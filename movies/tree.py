#!/usr/bin/env python

from movies import tmDB
from movies import imDB
from movies import omDB
from movies import rt
from tmdb3 import Person, Movie, List, Studio
import urllib2
import json
from util import jsonify

@jsonify
def getRTTree(movieId):
	rtJson = rt.getMovieInfo(movieId);
	# tmdbJson = tmDB.getMovieInfo(Movie(9340))
	result = {}
	rtInfo = json.loads(rtJson)
	# tmdbInfo = json.loads(tmdbJson)
	result["name"] = rtInfo["title"];
	#It will have Release Date, Run time, Ratings, Genre, Similar Movies, Cast, Studio, Revenue, Crew
	result["children"] = []
	# result["children"].append(createChild("Overview",tmdbInfo["overview"]))
	genres = []
	for g in rtInfo["genres"]:
		child = {}
		child["name"] = g
		genres.append(child)
	result["children"].append(createChildList("Genre",genres))
	releaseDates = []
	for r in rtInfo["release_dates"]:
		child = {}
		child["name"] = r + " = " + str(rtInfo["release_dates"][r])
		releaseDates.append(child)
	result["children"].append(createChild("Run Time",rtInfo["runtime"]))
	result["children"].append(createChildList("Release Dates",releaseDates))
	cast = []
	for c in rtInfo["cast"]:
		characters = []
		for char in c["characters"]:
			child = {}
			child["name"] = char
			characters.append(child)
		cast.append(createChildList(c["name"],characters))
	result["children"].append(createChildList("Cast",cast))
	# crew = []
	# for c in tmdbInfo["crew"]:
	# 	child = {}
	# 	child["name"] = c["job"] + " = " + c["name"]
	# 	crew.append(child)
	# result["children"].append(createChildList("Crew",crew))
	# studio = []
	# for s in tmdbInfo["studios"]:
	# 	child = {}
	# 	child["name"] = s["name"]
	# 	studio.append(child)
	# result["children"].append(createChildList("Studio",studio))
	# result["children"].append(createChild("Revenue",tmdbInfo["revenue"]))
	ratings = []
	for r in rtInfo["ratings"]:
		child = {}
		child["name"] = r + " = " + str(rtInfo["ratings"][r])
		ratings.append(child)
	result["children"].append(createChildList("Ratings",ratings))
	reviews = []
	for r in rtInfo["reviews"]:
		child = {}
		child["name"] = r["quote"]
		# child["name"] = '<a href = "%s">%s</a>'% (r["links"]["review"],r["publication"])
		reviews.append(child)
	result["children"].append(createChildList("Reviews",reviews))

	clips = []
	for r in rtInfo["clips"]:
		child = {}
		child["name"] = r["links"]["alternate"]
		# child["name"] = '<a href = "%s">%s</a>'% (r["links"]["review"],r["publication"])
		clips.append(child)
	result["children"].append(createChildList("Clips",clips))

	result["children"].append(createChild("Critics Consensus" , rtInfo["critics_consensus"]))
	similar = []
	for m in rtInfo["movies"]:
		ratings = []
		for r in m["ratings"]:
			child = {}
			child["name"] = r + " = " + str(m["ratings"][r])
			ratings.append(child)
		similar.append(createChildList(m["title"],ratings))
	result["children"].append(createChildList("Similar Movies",similar))
	
	return result

def createChildList(a,b):
	child = {}
	child["name"] = a
	child["children"] = b
	return child	

def createChild(a,b):
	child = {}
	child["name"] = a
	child["children"] = []
	child1 = {}
	child1["name"] = b	
	child["children"].append(child1)
	return child

if __name__ == '__main__':
	main()
	