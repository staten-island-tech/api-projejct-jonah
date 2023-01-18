
import os

from flask import Flask, render_template, request

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

    from .test import request1
    from .data import data2
    @app.route("/")
    def home():
        return render_template('home.html') 
    @app.route("/characters")
    def characters():
        param="/characters"
        data1=request1(param)
        if data1==0:
            return render_template("error.html")
        else:
            return render_template('characters.html',data=data1["data"]["results"])
    @app.route("/creators")
    def creators():
        param="/creators"
        data1=request1(param)
        if data1==0:
            return render_template("error.html")
        else:
            return render_template('creators.html',data=data1["data"]["results"])
    @app.route("/comics")
    def comics():
        param="/comics"
        data1=request1(param)
        if data1==0:
            return render_template("error.html")
        else:
            return render_template('comics.html',data=data1["data"]["results"])
    @app.route("/comic", methods=('GET', 'POST'))
    def comic():
        if request.method == "GET":
            type1="Comic"
            return render_template("ask.html", data2=data2["comics"],type1=type1)
        else:
            param1=request.form["title"]
            param="/comics/"+param1
            data1=request1(param)
            if data1==0:
                return render_template("error.html")
            else:
                return render_template('comic.html',data=data1["data"]["results"][0])
    @app.route("/character", methods=('GET', 'POST'))
    def character():
        if request.method == "GET":
            type1="Character"
            return render_template("ask.html", data2=data2["characters"],type1=type1)
        else:
            param1=request.form["title"]
            param="/characters/"+param1
            data1=request1(param)
            if data1==0:
                return render_template("error.html")
            else:
                return render_template('character.html',character=data1["data"]["results"][0])
    @app.route("/creator", methods=('GET', 'POST'))
    def creator():
        if request.method == "GET":
            type1="Creator"
            return render_template("ask.html", data2=data2["creators"],type1=type1)
        else:
            param1=request.form["title"]
            param="/creators/"+param1
            data1=request1(param)
            if data1==0:
                return render_template("error.html")
            else:
                return render_template('creator.html',character=data1["data"]["results"][0])
    @app.route("/events")
    def events():
        param="/events"
        data1=request1(param)
        if data1==0:
            return render_template("error.html")
        else:
            return render_template('events.html',data=data1["data"]["results"])
    @app.route("/series", methods=('GET', 'POST'))
    def series():
        if request.method == "GET":
            type1="Series"
            return render_template("ask.html", data2=data2["series"],type1=type1)
        else:
            param1=request.form["title"]
            param="/series/"+param1
            data1=request1(param)
            if data1==0:
                return render_template("error.html")
            else:
                return render_template('series.html',comic=data1["data"]["results"][0])
    @app.route("/serieses")
    def serieses():
        param="/series"
        data1=request1(param)
        if data1==0:
            return render_template("error.html")
        else:
            return render_template('serieses.html',data=data1["data"]["results"])
    @app.route("/event", methods=('GET', 'POST'))
    def event():
        if request.method == "GET":
            type1="Event"
            return render_template("ask.html", data2=data2["events"],type1=type1)
        else:
            param1=request.form["title"]
            param="/events/"+param1
            data1=request1(param)
            if data1==0:
                return render_template("error.html")
            else:
                return render_template('event.html',character=data1["data"]["results"][0])
    return app