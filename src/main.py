from flask import Flask, render_template, url_for
from qscraper import scrape_questions, scrape_quora


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard/')
def dashboard():
    queries = scrape_quora()
    return render_template('dashboard.html', queries=queries)


if __name__ == "__main__":
    app.run()
