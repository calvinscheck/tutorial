from flask import Flask, redirect, url_for, render_template, send_file
from flask import Blueprint, render_template
blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def index():
  return render_template('index/index.html')

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)

@blueprint.route('/cream')
def cream_me():
  return render_template('/index/index.html')