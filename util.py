#!/usr/bin/env python

import json

def jsonify(func):
	def JSON(dic):
		return json.dumps(func(dic))
	return JSON
