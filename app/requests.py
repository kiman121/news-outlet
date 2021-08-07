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
    query_string = 'top-headlines/sources'
    get_sources_url = base_url.format(query_string, api_key)
    # get_sources_url ='https://newsapi.org/v2/top-headlines/sources?apiKey=70a9b9d3f1624d63b54bf7ddd06b8c4d'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_results(source_list):
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
