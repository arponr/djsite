from django.contrib import admin
from blog.models import Category, Post, PostFile

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostFile)
