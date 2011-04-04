import sys
import os
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root_dir, 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def index():
    return render_template('index.html')

run_wsgi_app(app)

