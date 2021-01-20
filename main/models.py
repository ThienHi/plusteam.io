from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils import timezone


class Blog(models.Model):
    text = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = HTMLField(blank=True, null = True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="blog/")
    summary = models.TextField(max_length=500, blank=True, null = True, help_text="mô tả ngắn gọn cho bài viết")
    seo_descriptions = models.TextField(blank=True, null = True)
    figcaptions = models.TextField(blank=True, null = True, help_text="Tiêu đề của hình ảnh")
    view_count = models.IntegerField(default=0)
    create_at= models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "blog"
