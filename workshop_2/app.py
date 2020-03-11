import os
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)
students = []

@app.route("/")
def index():
  name = request.args.get("name", "world")
  return render_template("index.html", name=name)

@app.route("/registers")
def registers():
  print(students)
  return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
  name = request.form.get("name")
  email = request.form.get("email")
  dorm = request.form.get("dorm")
  if not name or not email or not dorm:
    return render_template("failure.html")

  msg = "You are registered!"
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  #server.login("c.chaiwat.ch@gmail.com", os.getenv("PASSWORD"))
  server.login("c.chaiwat.ch@gmail.com", "yai1784799")
  server.sendmail("c.chaiwat.ch@gmail.com", email, msg)
  return render_template("success.html")
