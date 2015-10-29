#!/usr/bin/env python

import argparse
import json
from flask import Flask, render_template
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

with open('data/flags.json', 'r') as f:
    flags = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

def unique(l):
    return sorted(set(l))

class Systems(Resource):
    def get(self):
        resp = { "results": unique(f["system"] for f in flags) }
        resp["status"] = 200
        return resp

class Applications(Resource):
    def get(self, sysname):
        resp = { "results": unique(f["application"] for f in flags if f["system"] == sysname) }
        resp["status"] = 200 if len(resp["results"]) > 0 else 404
        return resp

class Flags(Resource):
    def get(self, sysname, appname):
        resp = { "results": [f for f in flags if f["system"] == sysname
            and f["application"] == appname] }
        resp["status"] = 200 if len(resp["results"]) > 0 else 404
        return resp

api.add_resource(Systems, '/api/systems')
api.add_resource(Applications, '/api/apps/<string:sysname>')
api.add_resource(Flags, '/api/flags/<string:sysname>/<string:appname>')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', help='Address to bind.', default='127.0.0.1')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    app.run(debug=True, host=args.bind)
