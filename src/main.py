from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello, World!"

# @app.route("/")
# def index():
#     #return app.send_static_file('index.html')
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
