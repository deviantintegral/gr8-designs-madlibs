from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

DOCROOT = '/var/www/django-sites/gr8girls'

urlpatterns = patterns('',
    # Example:
    # (r'^gr8girls/', include('gr8girls.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'gr8girls.madlibs.views.index'),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': DOCROOT + '/madlibs/templates'}),
    (r'^data/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': DOCROOT + '/madlibs/data'}),
    (r'^(?P<user_name>\w+)/$', 'gr8girls.madlibs.views.list_madlibs'),
    (r'^(?P<user_name>\w+)/(?P<madlib_class>\w+)', 'gr8girls.madlibs.views.madlib'),
)
