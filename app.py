#!/usr/bin/env python

import argparse
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', help='Address to bind.', default='127.0.0.1')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    app.run(debug=True, host=args.bind)
