from flask import Flask, render_template
from qscraper import scrape


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def dashboard():
	queries = scrape()
	return render_template('dashboard.html', queries=queries)

if __name__ == "__main__":
    app.run()