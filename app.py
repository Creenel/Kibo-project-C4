from flask import Flask, requests, render_template, redirect, url_for, session
import pyrebase

app = Flask(__name__,template_folder = 'templates', static_folder = "static")
app.config["SECRET_KEY"] = "rotemthebest"

fbConfig = {
	"apiKey": "AIzaSyATvFI4Z5nj5VKP1Y16JGnAN2LcIk7ECUI",
	"authDomain": "kibo-project-8ea43.firebaseapp.com",
	"projectId": "kibo-project-8ea43",
	"storageBucket": "kibo-project-8ea43.appspot.com",
	"messagingSenderId": "1010392688942",
	"appId": "1:1010392688942:web:b334a7bf76efa442e8f2bf",
	"measurementId": "G-XFHXVES630",
	"databaseURL":"https://kibo-project-8ea43-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(fbConfig)
auth = firebase.auth()
db = firebase.database()

@app.route("/volunteer", methods = ["GET","POST"])
def volunteer():
    return render_template("volunteer.html")

@app.route("/main", methods = ["GET","POST"])
def volunteer():
    return render_template("main.html")

@app.route("/about", methods = ["GET","POST"])
def volunteer():
    return render_template("about.html")
    
@app.route("/host", methods = ["GET","POST"])
def volunteer():
     return render_template("host.html")


if (__name__) == "__main__":
  app.run(debug = True)

