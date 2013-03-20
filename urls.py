from django.conf.urls.defaults import patterns, include, url
from hc.settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hc.main.views.home', name='home'),
    url(r'^faq/$', 'hc.main.views.faq', name='faq'),
    url(r'^learn/$', 'hc.main.views.learn', name='learn'),
    url(r'^rules/$', 'hc.main.views.rules', name='rules'),
	url(r'^tour/(?P<nr>[\w|\W]+)/$', "hc.main.views.tour", name="tour"),
    url(r'^about/$', 'hc.main.views.about', name='about'),
    url(r'^stopspam/$', 'hc.main.views.stopspam', name='stopspam'),
    url(r'^spammerfame/$', 'hc.main.views.spammerfame', name='spammerfame'),
    url(r'^countries/$', 'hc.main.views.countries', name='countries'),
    url(r'^country/(?P<id>[\w|\W]+)/$', "hc.main.views.country", name="country"),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", dict(document_root = MEDIA_ROOT), name="media-root"),
    url(r"^static/(?P<path>.*)$", "django.views.static.serve", dict(document_root = MEDIA_ROOT), name="static-root"),   
    url(r'^accounts/', include('registration.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/$', include('forums.urls')),
    url(r'^logout/$', 'hc.main.views.logout', name='logout'),
    url(r'^accounts/profile/$', 'hc.main.views.profile', name='profile'),
)
