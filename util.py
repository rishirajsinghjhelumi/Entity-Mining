#!/usr/bin/env python

import json

def jsonify(func):
	def JSON(*args, **kwargs):
		return json.dumps(func(*args, **kwargs))
	return JSON
