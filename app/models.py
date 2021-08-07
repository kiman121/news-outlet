class Source:
    '''
    Source class that defines news Source objects
    '''

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


class Article:
    '''
    Airticle class that defines Article objects
    '''

    def __init__(self,source, author, title, description, article_url, image_url, published_at, content):
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

