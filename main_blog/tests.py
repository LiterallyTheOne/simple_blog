from django.test import TestCase
from .models import Post, Tag


class PostAndTagTestCase(TestCase):

    def setUp(self):
        self.p1 = Post(title="p1")
        self.p1.save()

        self.t1 = Tag(color=20, name="t1")
        self.t1.save()

        self.t2 = Tag(color=20, name="t2")
        self.t2.save()

        self.p1.tags.add(self.t1)
        self.p1.tags.add(self.t2)



    def test_tags_in_post(self):
        tags = self.p1.tags.all()

        self.assertEqual(len(tags), 2)

    def test_posts_in_tags(self):
        posts = self.t1.post_set.all()

        self.assertEqual(len(posts), 1)
