from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from blog.models import Post, Category
from optparse import make_option
from datetime import datetime

class Command(BaseCommand):
    option_list = (BaseCommand.option_list + 
                   (make_option('-e', action='store_true',
                                dest='edit', default=False),))

    def handle(self, *args, **options):
        with open('upload-temp') as f:
            sep = '\n' + ('%' * 70) + '\n'
            fields = f.read().split(sep)
            if options['edit']:
                try:
                    p = Post.objects.get(slug=fields[1])
                    p.edited = datetime.now()
                except Post.DoesNotExist:
                    raise CommandError('no post with slug "%s" exists'
                                       % fields[1]) 
            else:
                p = Post()
                p.created = datetime.now()
                p.edited = None
            p.title = fields[0]
            p.slug = fields[1]
            p.preview = fields[3]
            p.content = fields[4]
            p.save()
            for cat in fields[2].split(', '):
                try:
                    c = Category.objects.get(name=cat)
                except Category.DoesNotExist:
                    c = Category(name=cat, slug=slugify(cat))
                    c.save()
                p.categories.add(c)
            p.save()
                
                
            
