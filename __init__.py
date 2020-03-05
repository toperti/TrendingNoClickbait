from flask import Flask, render_template, request
from app import logic

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		filterTerm = request.form["search"]
		return render_template('home.html', videos = logic.getTrending(filterTerm.split()))
	return render_template('filter.html')