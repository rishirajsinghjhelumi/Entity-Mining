from app import app

@app.route("/",methods=['GET','POST'])
def indexPage():

	return "Entity Mining Web Application"

if __name__ == "__main__":

	app.run(host='0.0.0.0',debug=True)