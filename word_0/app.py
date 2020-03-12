from flask import Flask, render_template, request

app = Flask(__name__)
WORDS = []
with open("large", "r") as file:
  for line in file.readlines():
    WORDS.append(line.rstrip())

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/search")
def search():
  q = request.args.get("q")
  # Short Hand
  results = [word for word in WORDS if word.startswith(q)]
  # Full condition
  #words = []
  #for word in WORDS:
    #if word.startswith(q):
      #print(word)
      #words.append(word)
  return render_template("search.html", results=results)

