from django.db import models


class Tag(models.Model):
    color = models.IntegerField()
    name = models.CharField(max_length=20, unique=True)
    img = models.ImageField(upload_to='tag_images', default=None)
    url = models.URLField(default='', blank=True)
    description = models.TextField(default='no description yet')

    def __str__(self):
        return self.name

    @staticmethod
    def get_tags_order_by_more_posts():
        return Tag.objects.all().annotate(num_posts=models.Count('post')).order_by('-num_posts')


class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='post_images', default=None)
    description = models.TextField(default='no description yet')
    description_format = models.CharField(max_length=10, default='html',
                                          choices=[('html', 'html'), ('rst', 'rst'), ('md', 'md')])
    publish_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_date"]
