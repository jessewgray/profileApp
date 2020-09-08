import os
from flask import (Flask, render_template, send_from_directory, jsonify, request, redirect)
import mysql.connector
import os



app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "./static/uploads"



@app.route('/')
def index():
	return render_template('index.html', methods=['GET', 'POST'])


@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == "POST":

		if request.files:

			firstName = request.form["fName"]
			lastName = request.form["lName"]
			picture = request.files["picture"]
			
			userList = []
			params = {
		        "first_name": firstName,
		        "last_Name": lastName,
		        "picture": picture.filename
		        }


			picture.save(os.path.join(app.config["IMAGE_UPLOADS"], picture.filename))
			print(picture.filename + firstName)

			#return redirect(request.url)


		 	cnx = mysql.connector.connect(user="root", password="snowboarding", host="127.0.0.1", port=3306, database="people")
			mycursor = cnx.cursor()

			insertStatement = ('INSERT INTO people.person (firstName, lastName, profilePic) VALUES (%s, %s, %s)');
			insertData = (firstName, lastName, picture.filename)
			mycursor.execute(insertStatement, insertData)
			cnx.commit()


			userList.append(params)
			return jsonify(userList)

    

@app.route('/post', methods=['GET', 'POST'])
def post():
    return render_template('public/post.html', methods=['GET', 'POST'])


@app.route('/userjson', methods=['GET', 'POST'])
def userjson():
	cnx = mysql.connector.connect(user="root", password="snowboarding", host="127.0.0.1", port=3306, database="people")
	mycursor = cnx.cursor()
	mycursor.execute("SELECT * FROM people.person")
	myresult = mycursor.fetchall()
	personList = []
	content = {}

	for x in myresult:
		aPerson = {
			"num": x[0],
			"fName": x[1],
			"lName": x[2],
			"picture": x[3]
		}
		personList.append(aPerson)
	
	return jsonify(personList)


@app.route('/people', methods=['GET', 'POST'])
def people():
	return render_template('people.html', methods=['GET', 'POST'])




#test upload images

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            thename = request.form["fName"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print(thename)

            return redirect(request.url)


    return render_template("public/upload_image.html")



if __name__ == "__main__":
    app.run()


       

