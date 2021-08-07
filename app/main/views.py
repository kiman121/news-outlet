from flask import render_template, redirect, url_for
from . import main
from ..requests import get_sources
from ..models import Source, Article

@main.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''
    # Fecth sources
    news_sources = get_sources()
    title = 'Home - Welcome to the best News stream'

    return render_template('index.html', title = title, sources=news_sources)