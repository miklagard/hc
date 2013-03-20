import datetime
from django.core.cache import cache
from django.conf import settings
import redis

class ActiveUserMiddleware:
    def process_request(self, request):
        current_user = request.user
        if request.user.is_authenticated():
            now = datetime.datetime.now()
            #cache.set('seen_%s' % (current_user.username), now, settings.USER_LASTSEEN_TIMEOUT)
            redis.set(current_user.username, now)
            redis.expire(current_user.username, settings.USER_LASTSEEN_TIMEOUT)