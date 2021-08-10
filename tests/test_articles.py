import unittest
from app.models import Article


class TestReview(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("ktn-news", "KTN News",
                                   "Shishov case: Belarus leader Lukashenko denies link to dissident's death",
                                   "Alexander Lukashenko insists he had nothing to do with a suspicious hanging in Ukraine last week.",
                                   "https://www.standardmedia.co.ke/national/article/2001420415/court-paves-way-for-collymores-widow-to-distribute-vast-estate",
                                   "https://www.standardmedia.co.ke/national/article/2001420415/court-paves-way-for-collymores-widow-to-distribute-vast-estate",
                                   "2021-08-10T03:07:23.6456467Z",
                                   "media captionLukashenko: You can choke on your sanctions... you are American lapdogs Belarus's president has denied claims that his security services were involved in the death of dissident Vitaly… [+3443 chars")

    def tearDown(self):
        '''
        tearDown method cleans up after every test case run
        '''
        Article.clear_articles()

    def test_instance(self):
        '''
        test_instance test case to check if an instance has been created.
        '''
        self.assertTrue(isinstance(self.new_article, Article))

    def test_check_instance_variables(self):
        '''
        test_check_instance_variables test case to check instance variables.
        '''
        self.assertEqual(self.new_article.source, 'ktn-news')
        self.assertEqual(self.new_article.author, 'KTN News')
        self.assertEqual(self.new_article.title,
                         "Shishov case: Belarus leader Lukashenko denies link to dissident's death")
        self.assertEqual(self.new_article.description,
                         "Alexander Lukashenko insists he had nothing to do with a suspicious hanging in Ukraine last week.")
        self.assertEqual(self.new_article.article_url,
                         "https://www.standardmedia.co.ke/national/article/2001420415/court-paves-way-for-collymores-widow-to-distribute-vast-estate")
        self.assertEqual(self.new_article.image_url,
                         "https://www.standardmedia.co.ke/national/article/2001420415/court-paves-way-for-collymores-widow-to-distribute-vast-estate")
        self.assertEqual(self.new_article.published_at,
                         "2021-08-10T03:07:23.6456467Z")
        self.assertEqual(self.new_article.content,
                         "media captionLukashenko: You can choke on your sanctions... you are American lapdogs Belarus's president has denied claims that his security services were involved in the death of dissident Vitaly… [+3443 chars")

    def test_save_article(self):
        '''
        test_save_article test case that confirms if an article has been saved.
        '''
        self.new_article.save_article()
        self.assertTrue(len(Article.all_articles) > 0)

    def test_get_article_by_source(self):
        '''
        test_get_article_by_source test case that checks if an article object has been successfuly retrieved
        '''
        self.new_article.save_article()
        has_articles = Article.get_articles('ktn-news')
        self.assertTrue(len(has_articles) == 1)
