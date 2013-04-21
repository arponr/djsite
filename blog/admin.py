from django.contrib import admin
from blog.models import Category, Post, PostFile
from markdown import markdown
from datetime import datetime

class PostAdmin(admin.ModelAmin):    
    exclude = ('created', 'edited')

    def save_model(self, request, obj, form, change):
        obj.preview = markdown(obj.preview)
        obj.content = markdown(obj.content)
        if change:
            obj.edited = datetime.now()
        else:
            obj.created = datetime.now()
            obj.edited = None
        obj.save()

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostFile)
