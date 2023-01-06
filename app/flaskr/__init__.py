import os

from flask import Flask, render_template
from .tempdata import data

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .test import request
    @app.route("/")
    def home():
        return render_template('home.html') 
    @app.route("/characters")
    def characters():
        param="/characters"
        data1=request(param)
        return render_template('characters.html',data=data1["data"]["results"])
    @app.route("/creators")
    def creators():
        param="/creators"
        data1=request(param)
        return render_template('creators.html',data=data1["data"]["results"])
    @app.route("/comics")
    def comics():
        param="/comics"
        data1=request(param)
        return render_template('comics.html',data=data1["data"]["results"])
    @app.route("/comic/<path:Id>")
    def comic(Id):
        #Id=43257
        param="/comics/"+Id
        data1=request(param)
        print(data1)
        return render_template('comic.html',data=data1["data"]["results"])
    return app