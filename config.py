import os

class Config:
    '''
    Class that has the general application configurations   
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Class that details production configurations
    Args:
        Config: The parent configuration class with general 
        application configurations
    '''
    pass

class DevConfig(Config):
    '''
    Class that details development configurations
    Args:
        Config: The parent configuration class with general 
        application configurations
    '''
    DEBUG = True

# Different configuration options
config_options = {
    'development':DevConfig,
    'production': ProdConfig
}