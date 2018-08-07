from flask import Flask, render_template, url_for
from qscraper import scrape_questions


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
	queries = scrape_questions()
	return render_template('dashboard.html', queries=queries)

if __name__ == "__main__":
    app.run()