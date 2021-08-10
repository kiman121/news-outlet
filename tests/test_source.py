import unittest
from app.models import Source


class TestReview(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("ktn-news", "KTN News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines.",
                                 "https://www.standardmedia.co.ke/", "general", "en", "ke")

    def tearDown(self):
        '''
        tearDown method cleans up after every test case run
        '''
        Source.clear_sources()

    def test_instance(self):
        '''
        test_instance test case to check if an instance has been created.
        '''
        self.assertTrue(isinstance(self.new_source, Source))

    def test_check_instance_variables(self):
        '''
        test_check_instance_variables test case to check instance variables.
        '''
        self.assertEqual(self.new_source.id, 'ktn-news')
        self.assertEqual(self.new_source.name, 'KTN News')
        self.assertEqual(self.new_source.description,
                         'Your trusted source for breaking news, analysis, exclusive interviews, headlines.')
        self.assertEqual(self.new_source.url,
                         'https://www.standardmedia.co.ke/')
        self.assertEqual(self.new_source.category, 'general')
        self.assertEqual(self.new_source.language, 'en')
        self.assertEqual(self.new_source.country, 'ke')

    def test_save_source(self):
        '''
        test_save_source test case that confirms if a source has been saved.
        '''
        self.new_source.save_source()
        self.assertTrue(len(Source.all_sources) > 0)
    
    def test_get_source_by_id(self):
        '''
        test_get_source_by_id test case that checks if an object has been successfuly retrieved
        '''
        self.new_source.save_source()
        has_sources = Source.get_sources('ktn-news')
        self.assertTrue(len(has_sources) == 1)