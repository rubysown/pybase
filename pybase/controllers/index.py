# -*- coding: utf-8 -*-
import json
from pybase import app
from flask import render_template, request

@app.route('/')
def start():
    return json.dumps({})
