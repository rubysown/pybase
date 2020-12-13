import os
from flask import Flask

__version__ = '0.1'
app = Flask('pybase')
app.config['SECRET_KEY'] = 'random'

debug = True
if os.environ.get('DEBUG'):
    debug = os.environ.get('DEBUG')
app.debug = debug

from pybase.controllers import *
