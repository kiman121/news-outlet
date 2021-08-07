from flask import render_template, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
# from ..models import Source, Article


@main.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''
    # Fetch sources
    news_sources = get_sources()
    title = 'Home - Welcome to the best News stream'

    return render_template('index.html', title=title, sources=news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns the articles page for the selected news source
    '''
    #Fetch articles
    articles = get_articles(source_id)
    
    return render_template('news-articles.html', articles = articles)


