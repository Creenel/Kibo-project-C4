
from flask import Flask, request, render_template, redirect, url_for, session
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
  if request.method == "POST":
    user = auth.create_user_with_email_and_password(request.form['email'],request.form['password'])
    user['name'] = request.form['full_name']
    user['age'] = request.form['age']
    user['language'] = request.form['language']
    user['location'] = request.form['location']
    session['user'] =user
    session['userID'] = session['user']["localId"]
    db.child("Volunteers").child(session["userID"]).set(session['user'])
    return redirect(url_for("main"))
  else:
    return render_template("volunteer.html")

@app.route("/", methods = ["GET","POST"])
def main():
    return render_template("main.html")

@app.route("/about", methods = ["GET","POST"])
def about():
    return render_template("about.html")
    
@app.route("/host", methods = ["GET","POST"])
def host():
     return render_template("host.html")

@app.route("/profile",methods = ["GET","POST"])
def profile():
  return render_template("profile.html", userdic = session['user'])

@app.route("/pic", methods = ["GET","POST"])
def pic():
  if request.method == "POST":
    db.child("Images").push(request.form["imgsrc"])
    return redirect(url_for("gallery"))
  else:
    return render_template("pic.html")

@app.route("/gallery", methods = ["GET","POST"])
def gallery():
  return render_template("gallery.html", imgdic = db.child("Images").get().val())

@app.route("/signin", methods = ["GET","POST"])
def signin():
  if request.method == "POST":
    session['user'] = auth.sign_in_with_email_and_password()
    return redirect(url_for("main"))
  else:
    return render_template("signin.html")

@app.route("/remove",methods = ["GET","POST"])
def remove():
  print(session["userID"])
  db.child("Volunteers").child(session["userID"]).remove()
  session['user'] = None
  session['userID'] = None
  auth.current_user = None
  return redirect(url_for("main"))

@app.route("/signout",methods = ["GET","POST"])
def signout():
  print(session["userID"])
  session['user'] = None
  session['userID'] = None
  auth.current_user = None
  return redirect(url_for("main"))


if (__name__) == "__main__":
  app.run(debug = True)
