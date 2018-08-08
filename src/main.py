from flask import Flask, render_template, url_for, request
from wtforms import Form, TextAreaField, validators
from qscraper import scrape_questions, scrape_quora


app = Flask(__name__)

class SearchForm(Form):
	inputString = TextAreaField('Query', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard/')
def dashboard():
	return render_template('dashboard.html', queries=[])

@app.route('/results/', methods=['POST'])
def results():
	form = SearchForm(request.form)
	queries = []
	if request.method == 'POST' and form.validate():
		search = request.form['search']
		queries = scrape_quora(search)
		return redirect(url_for('dashboard'))
	return render_template('dashboard.html', queries=queries)

if __name__ == "__main__":
    app.run(debug=True)
