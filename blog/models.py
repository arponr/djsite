from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog.views.category', args=[self.slug])

    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created = models.DateTimeField()
    edited = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', 
                       args=[self.created.year, 
                             self.created.month,
                             self.slug])

    class Meta:
        ordering = ['-created']
