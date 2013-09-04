# -*- coding:utf-8 -*-
from django.core.cache import cache
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from datetime import datetime

# Maximum page view time (in seconds).
USER_PAGE_VIEW_TIME = 2 * 60

CACHE_ONLINE_USER_ID_PREFIX = "online_u_"
CACHE_ONLINE_USER_SESSION_PREFIX = "online_s_"
CACHE_ONLINE_USERS_KEY = "online_xusers"

if settings.SESSION_ENGINE != "django.contrib.sessions.backends.db":
    raise Exception("Online users middleware supports only 'django.contrib.sessions.backends.db' session engine.")    

def get_cache_key_for_session(session_key):
    return "%s%s" % (CACHE_ONLINE_USER_SESSION_PREFIX, session_key)

def get_online_users():
    # Retrieving all users from cache.
    registered_users = {}
   
    # Iterating users.
    try:
        users = cache.get(CACHE_ONLINE_USERS_KEY, {})
    except:
        users = {}
    fresh_users = {}

    for id, user in users.iteritems():
        cached_user = cache.get(get_cache_key_for_session(id), False)
        if cached_user:
            if cached_user != "":
                fresh_users[id] = cached_user
                registered_users[cached_user] = cached_user
    cache.set(CACHE_ONLINE_USERS_KEY, fresh_users, USER_PAGE_VIEW_TIME)    
   
    return registered_users.values()

def add_online_user(request):
	users = cache.get(CACHE_ONLINE_USERS_KEY, {})
	if request.user.is_authenticated():
		users[request.session.session_key] = request.user.username
		cache.set(get_cache_key_for_session(request.session.session_key), request.user.username, USER_PAGE_VIEW_TIME)
	else:
		users[request.session.session_key] = True
		cache.set(get_cache_key_for_session(request.session.session_key), True, USER_PAGE_VIEW_TIME)
	cache.set(CACHE_ONLINE_USERS_KEY, users, USER_PAGE_VIEW_TIME)

class OnlineUsers(object):
    def process_request(self, request):
        if not request.path.endswith("/"):
            return
       
        # Django don't stores anonymous session if it isn't used by any module. So we force session saving.
        if request.user.is_anonymous and Session.objects.filter(session_key=request.session.session_key).filter(expire_date__gt=datetime.now()).count() == 0:
            request.session.save()
            request.session.modified = True
        # Storing last user page view time in cache according to session key. Cache time is equal to maximum page view time.
        # Illegal or empty session cookie causes ignoring request (auth middlewate loads real session so session key is true)
        if request.COOKIES.get(settings.SESSION_COOKIE_NAME, None) == request.session.session_key:
            add_online_user(request)