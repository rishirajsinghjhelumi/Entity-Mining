from app import app

from flask import render_template

import movies.views
import music.views

@app.route("/",methods=['GET'])
def indexPage():

	return render_template('index.html')

@app.route("/report",methods=['GET'])
def reportPage():

	return render_template('report.html')

if __name__ == "__main__":

	app.run(host='0.0.0.0',debug=True)