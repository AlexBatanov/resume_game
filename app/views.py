from flask import render_template

from app.services import add_visitions, get_visitions
from app import app


@app.route('/')
def index():
    add_visitions()
    return render_template('resume_game.html')


@app.route('/count')
def number_visitors():
    return f'Total visits: {get_visitions()}'
