from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_sources()
    title = "NewsSource - Your trusted source of news!"
    return render_template('index.html', title=title, sources=source)