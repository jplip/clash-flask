import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.characters import initCharacters
from model.common import initCommon
from model.rare import initRare
from model.epic import initEpic
from model.legendary import initLegendary
from model.champion import initChampion

# setup APIs
from api.characters import characters_api
from api.common import common_api
from api.rare import rare_api
from api.epic import epic_api
from api.legendary import legendary_api
from api.champion import champion_api

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(characters_api)
app.register_blueprint(common_api)
app.register_blueprint(rare_api)
app.register_blueprint(epic_api)
app.register_blueprint(legendary_api)
app.register_blueprint(champion_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():  # activate these items
    initCharacters()
    initCommon()
    initRare()
    initEpic()
    initLegendary()
    initChampion()
# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8113")
