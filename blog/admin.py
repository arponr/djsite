from django.contrib import admin
from blog.models import Category, Post, PostFile
from datetime import datetime

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PostFileInline(admin.TabularInline):
    model = PostFile

class PostAdmin(admin.ModelAdmin):    
    exclude = ('created', 'edited')
    inlines = [PostFileInline,]
    prepopulated_fields = {'slug':('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20,
                                                     'cols':70})}
    }

    def save_model(self, request, obj, form, change):
        if change:
            obj.edited = datetime.now()
        else:
            obj.created = datetime.now()
            obj.edited = None
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostFile)
