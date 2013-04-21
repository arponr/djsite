from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    ('^$', 'blog.views.blog'),
    ('^work/$', 'djsite.views.work'),
    (r'^category/([-\w]+)/$', 'blog.views.category'),
    (r'^post/([-\w]+)/$', 'blog.views.post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT,}), 
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_ROOT,}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
