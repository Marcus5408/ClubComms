import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('home.html')


@app.route('/about')
def about():
    return flask.render_template(f'{__file__.replace("__init__.py","")}src\\about.html')




if __name__ == '__main__':
    app.run(debug=True)