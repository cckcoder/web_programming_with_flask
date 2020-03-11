from flask import Flask, render_template, request

app = Flask(__name__)
students = []

@app.route("/")
def index():
  name = request.args.get("name", "world")
  return render_template("register.html", name=name)

@app.route("/registers")
def registers():
  print(students)
  return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
  name = request.form.get("name")
  dorm = request.form.get("dorm")
  if not name or not dorm:
    return render_template("failure.html")
  students.append(f"{name} from {dorm}")
  return render_template("success.html")
