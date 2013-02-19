from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

from django.contrib import admin

urlpatterns = patterns('',
    url(r'', 'hc.apps.main.views.start', name='start'),

)