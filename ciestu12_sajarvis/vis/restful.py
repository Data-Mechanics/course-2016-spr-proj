# Make our db accessible over REST, with authentication.
from flask import Flask
from flask import request
from flask import send_from_directory
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)

exec(open('../../pymongo_dm.py').read())
teamname = 'ciestu12_sajarvis'
client = pymongo.MongoClient()
repo = client.repo
repo.authenticate(teamname, teamname)

@app.route('/')
def index():
    return """Nothing here, try
        <a href=\"./stops\">/stops</a> or
        <a href=\"./utility\">/utility</a>.
        """

@app.route('/stops')
def loadmap():
    '''Load the static file. To change the visualization change the js file.'''
    d = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(d, 'vis'), 'optimal_stops.html')

@app.route('/utility')
def loadutil():
    '''Load the static file. To change the visualization change the js file.'''
    d = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(d, 'vis'), 'utility.html')

@app.route('/get/<collection>')
def getthings(collection):
    '''Query the database from js in browser.'''
    # If you have a collection with 'name':<name> in the documents, filter
    # on a name with query args like /collection?name=<name>
    args = {}
    for k in request.args.keys():
        try:
            # Mongo will not be flexible with types
            args[k] = int(request.args[k])
        except ValueError:
            args[k] = request.args[k]
    all_stops = repo['{}.{}'.format(teamname, collection)].find(args)
    return dumps(all_stops)

if __name__ == '__main__':
    app.run(debug=True)
