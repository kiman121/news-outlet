from flask import render_template, redirect, url_for, request
from . import main
from ..requests import get_sources, get_articles, get_article


@main.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''
    # Fetch sources
    news_sources = get_sources()
    title = 'Home - Welcome to the best News stream'

    return render_template('index.html', title=title, sources=news_sources)


@main.route('/articles', methods=['GET'])
def articles():
    '''
    Function that returns the articles page for the selected news source
    '''
    query_string = request.args.to_dict()
    source_id = query_string['source_id']

    article_title = None

    if len(query_string) > 1:
        title_split = query_string['article_title'].split(" ")
        article_title = '+'.join(title_split)
    # Fetch articles
    articles = get_articles(source_id)

    main_article = get_article(source_id, article_title)

    return render_template('news-articles.html', articles=articles, main_article=main_article)
