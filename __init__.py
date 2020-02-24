from flask import Flask, render_template
from app import logic

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', videos = logic.getTrending())
