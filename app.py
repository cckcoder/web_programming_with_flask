from flask import Flask, render_template, request

app = Flask(__name__)
student = []

@app.route("/")
def index():
  name = request.args.get("name", "world")
  return render_template("register.html", name=name)

@app.route("/registers")
def registers():
  return render_template("registered.html", student=student)

@app.route("/register", methods=["POST"])
def register():
  name = request.form.get("name")
  dorm = request.form.get("dorm")
  if not name or not dorm:
    return render_template("failure.html")
  student.append(f"{name} from {dorm}")
  return render_template("success.html")
