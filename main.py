from app import app

import movies.views
import music.views

@app.route("/",methods=['GET'])
def indexPage():

	return "Entity Mining Web Application"

if __name__ == "__main__":

	app.run(host='0.0.0.0',debug=True)