class Source:
    '''
    Class that defines news Source objects
    '''
    all_sources = []

    def __init__(self, id, name, description, url, category, language, country):
        '''
        __init__ method helps in defining properties for the source object.
        Args:
            id: New source id.
            name : New source name.
            description: New source description
            url: New source url
            category: New source category
            language: New source language
            country: New source country
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    def save_source(self):
        '''
        Method that saves a source
        '''
        Source.all_sources.append(self)

    @classmethod
    def clear_sources(cls):
        '''
        Method that resets the all_sources list
        '''
        Source.all_sources.clear()

    @classmethod
    def get_sources(cls, id):
        '''
        Method that retieves a source
        '''
        results = []
        for source in cls.all_sources:
            if source.id == id:
                results.append(source)
        
        return results
        
class Article:
    '''
    Class that defines Article objects
    '''
    all_articles = []

    def __init__(self, source, author, title, description, article_url, image_url, published_at, content):
        '''
        __init__ method helps in defining properties for the article object.
        Args:
            author: New article author.
            title : New article title.
            description: New article description
            article_url: New article url
            image_url: New article image url
            publishe_at: New article publish at (date)
            content: New article content
        '''
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.article_url = article_url
        self.image_url = image_url
        self.published_at = published_at
        self.content = content

    def save_article(self):
        '''
        Method that saves as article
        '''
        Article.all_articles.append(self)

    @classmethod
    def clear_articles(cls):
        '''
        Method that resets the all_articles list
        '''
        Article.all_articles.clear()

    @classmethod
    def get_articles(cls, source):
        '''
        Method that retieves an article
        '''
        results = []
        for article in cls.all_articles:
            if article.source == source:
                results.append(article)
        
        return results