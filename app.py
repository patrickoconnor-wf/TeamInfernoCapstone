#!/usr/bin/env python

import argparse
from flask import Flask, render_template
from flask_restful import Resource, Api, abort
import json


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

class SystemList(Resource):
    """
    A class for a list of Systems.
    :param self: The request that triggered this response
    :return resp: A Response object with the requested data and a status code.
    """
    def get(self):
        json_str = open('systems.json').read()
        resp = json.loads(json_str)
        resp['status'] = 200

        return resp

class ApplicationList(Resource):
    """
    A class for a list of Applications.
    :param self: The request that triggered this response
    :return resp: A Response object with the requested data and a status code.
                  Returns a 400 if the Application cannot be found.
    """
    def get(self, system_name):
        systems = {'com': 'ch_applications.json', 'mobileapps': 'ma_applications.json'}
        if system_name in systems:
            json_str = open(systems[system_name]).read()
            resp = json.loads(json_str)
            resp['status'] = 200
        else:
            abort(400, message="System Not Found.")

        return resp
        
class FeatureFlagList(Resource):
    """
    A class for a list of FeatureFlags.
    :param self: The request that triggered this response
    :return resp: A Response object with the requested data and a status code.
                  Returns a 400 if the Application or System cannot be found.
    """
    def get(self, system_name, application_name):
        systems = {'com': 'com', 'mobileapps': 'mobileapps'}
        applications = {'com': 'ch_app_ch.json'}
        if system_name in systems:
            if application_name in applications:
                json_str = open(applications[systems[system_name]]).read()
                print(json_str)
                resp = json.loads(json_str)
                resp['status'] = 200
                return resp
            else:
                abort(400, message="Application Not Found")
        else:
            abort(400, message='System Not Found')


api.add_resource(SystemList, '/api/systems/')
api.add_resource(ApplicationList, '/api/systems/<string:system_name>/')
api.add_resource(FeatureFlagList, '/api/systems/<string:system_name>/applications/<string:application_name>/')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', help='Address to bind.', default='127.0.0.1')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    app.run(debug=True, host=args.bind)
