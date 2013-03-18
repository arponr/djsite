from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from blog.models import Post, Category
from optparse import make_option
from datetime import datetime

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (make_option('--update'),)

    def handle(self, *args, **options):
        with open('upload-temp') as f:
            _title = f.readline().rstrip()
            _slug = f.readline().rstrip()
            _cats = f.readline().rstrip().split(', ')
            _content = f.read().lstrip()
            if options['update']:
                try:
                    p = Post.objects.get(slug=_slug)
                    p.edited = datetime.now()
                except Post.DoesNotExist:
                    raise CommandError('no post with slug "%s" exists'
                                       % _slug) 
            else:
                p = Post()
                p.created = datetime.now()
                p.edited = None
            p.title = _title
            p.slug = _slug
            p.content = _content
            p.save()
            for cat in _cats:
                try:
                    c = Category.objects.get(name=cat)
                except Category.DoesNotExist:
                    c = Category(name=cat, slug=slugify(cat))
                    c.save()
                p.categories.add(c)
            p.save()
                
                
            
