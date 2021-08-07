import urllib.request
import json
from .models import Source, Article

# Global variables
api_key = None
base_url = None


def configure_request(app):
    '''
    Function that takes application instance and sets configuration values to 
    api_key and base_url variables
    '''
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    Function that gets the news sources json response to the url request
    https://newsapi.org/v2/top-headlines/sources?apiKey=70a9b9d3f1624d63b54bf7ddd06b8c4d
    '''
    page_resource = 'top-headlines/sources?apiKey={}'.format(api_key)
    get_sources_url = base_url.format(page_resource)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)

    return source_results


def process_sources(source_list):
    '''
    Function that processes the source result and transforms to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if id:
            source_object = Source(id, name, description,
                                   url, category, language, country)
            source_results.append(source_object)

    return source_results


def get_article(source_id, article_title):
    '''
    Function that gets the top most article
    https://newsapi.org/v2/top-headlines?sources=bbc-news&pageSize=1&apiKey=70a9b9d3f1624d63b54bf7ddd06b8c4d
    '''

    if article_title != None:
        page_resource = f'top-headlines?sources={source_id}&q={article_title}&apiKey={api_key}'
    else:
        page_resource = f'top-headlines?sources={source_id}&pageSize=1&apiKey={api_key}'

    article_url = base_url.format(page_resource)
    # article_url='https://newsapi.org/v2/top-headlines?sources=bbc-news&pageSize=1&apiKey=70a9b9d3f1624d63b54bf7ddd06b8c4d'

    with urllib.request.urlopen(article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_result = None

        if get_article_response['articles']:

            article = get_article_response['articles'][0]

            source = source_id
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            article_url = article.get('url')
            image_url = article.get('urlToImage')
            published_at = article.get('publishedAt')
            content = article.get('content')

            article_result = Article(
                source, author, title, description, article_url, image_url, published_at, content)

    return article_result


def get_articles(source_id):
    '''
    Function that gets news articles for a selected sources

    https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=70a9b9d3f1624d63b54bf7ddd06b8c4d

    '''
    page_resource = 'top-headlines?sources={}&apiKey={}'.format(
        source_id, api_key)
    get_articles_url = base_url.format(page_resource)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_result = None

        if get_articles_response['articles']:
            articles_result_list = get_articles_response['articles']
            articles_result = process_articles(articles_result_list, source_id)

    return articles_result


def process_articles(articles_list, source_id):
    '''
    Function that process the articles result and transforms to a list of objects
    Args:
        articles_list: A list of dictionaries that contain articles detail
    Return:
        articles_result: A list of article objects
    '''
    articles_result = []

    for article_item in articles_list:
        source = source_id
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        article_url = article_item.get('url')
        image_url = article_item.get('urlToImage')
        published_at = article_item.get('publishedAt')
        content = article_item.get('content')

        if author:
            article_object = Article(
                source, author, title, description, article_url, image_url, published_at, content)
            articles_result.append(article_object)

    return articles_result
