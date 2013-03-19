from django.conf.urls.defaults import patterns, include, url
from hc.settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hc.main.views.home', name='home'),
    # url(r'^hc/', include('hc.foo.urls')),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", dict(document_root = MEDIA_ROOT), name="media-root"),
    url(r"^static/(?P<path>.*)$", "django.views.static.serve", dict(document_root = MEDIA_ROOT), name="static-root"),   
    url(r'^accounts/', include('registration.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
