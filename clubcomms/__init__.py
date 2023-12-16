import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('clubcomms.html')


if __name__ == '__main__':
    app.run(debug=True)