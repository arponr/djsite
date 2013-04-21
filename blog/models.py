from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    icon = models.FileField(upload_to='icons', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog.views.category', args=[self.slug])

    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    public = models.BooleanField()
    preview = models.TextField()
    content = models.TextField()
    created = models.DateTimeField()
    edited = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

    class Meta:
        ordering = ['-created']

class PostFile(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='%Y/%m/%d')
    post = models.ForeignKey('Post')
