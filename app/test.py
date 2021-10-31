import unittest
from models import source, article

Source=source.Source
Article=article.Article
class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs', 'general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
        
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("John",'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs', 'https://image.tmdb.org/', 'October')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))        
        
if __name__ == '__main__':
    unittest.main()        