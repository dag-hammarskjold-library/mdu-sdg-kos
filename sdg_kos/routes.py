from flask import Flask, render_template, request, abort, jsonify, Response, url_for
from flask_babel import Babel, gettext
from requests import get
from app.lib.poolparty import PoolParty, Thesaurus
from app.config import Config
from app import cache, app
import boto3, re, time, os

pool_party = PoolParty(Config.endpoint, Config.project_id, Config.username, Config.password)
thesaurus = Thesaurus(pool_party)

# And start building your routes.
@app.route('/')
def index():
    return_data = thesaurus.get_concept(concept='http://metadata.un.org/sdg/kos')
    return render_template('index.html', data=return_data)

@app.route('/<id>')
def get_concept_landing(id):
    return_data = thesaurus.get_concept(concept='http://metadata.un.org/sdg/kos/%s' % id)
    return render_template('index.html', data=return_data)