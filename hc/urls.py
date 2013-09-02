from django.conf.urls.defaults import patterns, include, url
from hc.settings import STATIC_ROOT, MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hc.views.home', name='home'),
    url(r'^faq/$', 'hc.views.faq', name='faq'),
    url(r'^learn/$', 'hc.views.learn', name='learn'),
    url(r'^rules/$', 'hc.views.rules', name='rules'),
	url(r'^tour/(?P<nr>[\w|\W]+)/$', "hc.views.tour", name="tour"),
    url(r'^about/$', 'hc.views.about', name='about'),
    url(r'^countries/$', 'hc.views.countries', name='countries'),
    url(r'^country/(?P<id>[\w|\W]+)/$', "hc.views.country", name="country"),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", dict(document_root = MEDIA_ROOT), name="media-root"),
    url(r"^static/(?P<path>.*)$", "django.views.static.serve", dict(document_root = STATIC_ROOT), name="static-root"),   
    url(r'^accounts/', include('registration.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
