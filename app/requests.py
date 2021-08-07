import urllib.request,json
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
