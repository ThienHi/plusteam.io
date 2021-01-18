from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Blog(models.Model):
    text = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = HTMLField(blank=True, null = True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_blog_post', None, {'slug': self.slug})

    class Meta:
        db_table = "blog"
