from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Author')

        self.assertEqual(b.__repr__(), 'Test by Author (0 posts)')

