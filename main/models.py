from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils import timezone

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def count_post(self):
        return Blog.objects.filter(category=self).count()

    count_post.allow_tags = True
    class Meta:
        db_table = "blog_category"
        ordering = ['-id']


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE)
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

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "blog"
        ordering=["-id"]
        

class Email(models.Model):
    name = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-id']
        db_table = 'emails'
