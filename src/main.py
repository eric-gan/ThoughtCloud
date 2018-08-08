from flask import Flask, render_template, url_for, request
from qscraper import scrape_questions, scrape_quora


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results/')
def results(queries=None):
    print(queries)
    return render_template('results.html', queries=queries)


@app.route('/search/')
def search():
    print('started results')
    return render_template('search.html')


@app.route('/search/', methods=['POST'])
def search_requested():
    print('got here')
    search_results = []
    search_input = request.form['search']
    search_results = scrape_quora(search_input)
    return results(queries=search_results)


if __name__ == "__main__":
    app.run(debug=True)
