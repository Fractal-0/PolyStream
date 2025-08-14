import flask

app = flask.Flask(__name__)

MANIFEST = '''
{
  "id": "com.stremio.PolyTest.addon",
  "version": "0.0.15",
  "name": "Test",
  "description": "Testing for PolyStream",
  "catalogs": [],
  "resources": [
    {
      "name": "stream",
      "types": [
        "movie",
        "series",
        "anime"
      ],
      "idPrefixes": [
        "tt",
        "kitsu"
      ]
    }
  ],
  "types": [
    "movie",
    "series",
    "anime",
    "other"
  ],
  "behaviorHints": {
    "configurable": true,
    "configurationRequired": false
  }
}'''

def respond_with(data):
    resp = flask.Response(data, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp

@app.route('/manifest.json')
def manifest():
    return respond_with(MANIFEST)

@app.route('/stream/<type>/<id>.json')
def stream(type, id):
    print(flask.request.content_length)
    print(flask.request.headers)
    return "", 404

app.run(debug = True)

