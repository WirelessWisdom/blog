from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Author')
        b.create_post('Test title', 'Test content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test title')
        self.assertEqual(b.posts[0].content, 'Test content')

    def test_json(self):
        b = Blog('Test', 'Author')
        b.create_post('Test title', 'Test content')

        expected = {'title': 'Test',
                    'author': 'Author',
                    'posts': [{'title': 'Test title', 'content': 'Test content'}]}

        self.assertDictEqual(b.json(), expected)

    def test_json_no_posts(self):
        b = Blog('Test', 'Author')

        expected = {'title': 'Test',
                    'author': 'Author',
                    'posts': []}
        self.assertDictEqual(b.json(), expected)



