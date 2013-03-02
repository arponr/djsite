from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    intro = models.TextField()
    content = models.TextField()
    created = models.DateTimeField()
    edited = models.DateTimeField()
    tags = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']
