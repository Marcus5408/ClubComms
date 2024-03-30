import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("clubcomms.html")


@app.route("/demo/")
def demo():
    return flask.render_template("demo.html", url=flask.url_for('static', filename='demo'))


@app.route("/demo/<path:path>")
def media(path):
    return flask.send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run(debug=True)
