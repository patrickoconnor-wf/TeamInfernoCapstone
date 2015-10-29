#!/usr/bin/env python

import argparse
import json
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from fuzzywuzzy import fuzz

app = Flask(__name__)
api = Api(app)

with open('data/flags.json', 'r') as f:
    flags = json.load(f)

def extract(json):
    '''Extracts all strings from a JSON hierarchy
    '''
    if isinstance(json, dict):
        return ' '.join(extract(v) for v in json.values())
    if isinstance(json, list):
        return ' '.join(extract(v) for v in json)
    if isinstance(json, basestring):
        return str(json)
    return ''

corpus = { f['name']: extract(f) for f in flags }

@app.route('/')
def index():
    return render_template('index.html')

def unique(l):
    return sorted(set(l))

class Systems(Resource):
    def get(self):
        resp = { "results": unique(f["system"] for f in flags) }
        resp["status"] = 200
        return resp, resp["status"]

class Applications(Resource):
    def get(self, sysname):
        resp = { "results": unique(f["application"] for f in flags if f["system"] == sysname) }
        resp["status"] = 200 if len(resp["results"]) > 0 else 404
        return resp, resp["status"]

class Flags(Resource):
    def get(self, sysname, appname):
        resp = { "results": [f for f in flags if f["system"] == sysname
            and f["application"] == appname] }
        resp["status"] = 200 if len(resp["results"]) > 0 else 404
        return resp, resp["status"]

class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q', type=str)
        args = parser.parse_args()
        query = args['q']
        return { 'results': self.search(query), 'status': 200 }

    def search(self, query):
        tuples = [(f, fuzz.token_set_ratio(query, corpus[f['name']])) for f in flags]
        tuples = [t for t in tuples if t[1] >= 25]
        tuples.sort(key=lambda t: -t[1])
        return [t[0] for t in tuples]


api.add_resource(Systems, '/api/systems')
api.add_resource(Applications, '/api/apps/<string:sysname>')
api.add_resource(Flags, '/api/flags/<string:sysname>/<string:appname>')
api.add_resource(Search, '/api/search')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', help='Address to bind.', default='127.0.0.1')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    app.run(debug=True, host=args.bind)
