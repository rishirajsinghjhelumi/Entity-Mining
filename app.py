#!/usr/bin/env python

from flask import Flask, render_template, jsonify
import os

templateDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/templates')

app = Flask(__name__, template_folder = templateDirectory)
app.config.from_object(__name__)


@app.errorhandler(403)
def forbidden_page(error):
	return 	jsonify(status = "Forbidden Page"), 403

@app.errorhandler(404)
def page_not_found(error):
	return jsonify(status = "Page Not Found"), 404

@app.errorhandler(500)
def server_error_page(error):
	return jsonify(status = "Server Error"), 500