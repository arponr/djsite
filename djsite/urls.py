from django.conf.urls import patterns, include, url
from djsite.views import about, resume, work
from blog.views import blog, post

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^about/$', about),
                       ('^resume/$', resume),
                       ('^work/$', work),
                       ('^$', blog),
                       (r'^post/(\d+)/$', post),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
