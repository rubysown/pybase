import json
from pybase.app import app

@app.route('/')
def start():
    return json.dumps({})
