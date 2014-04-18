#!/usr/bin/env python

import json
from flask import Response

def jsonify(func):
	def JSON(*args, **kwargs):
		return json.dumps(func(*args, **kwargs), indent = 4)
	return JSON

def ResponseJSON(responseText):
	return Response(response=responseText, status=200, mimetype='application/json')