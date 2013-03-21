import datetime
from django.core.cache import cache
from django.conf import settings
import redis 

class ActiveUserMiddleware:

    def process_request(self, request):
        current_user = request.user

        if request.user.is_authenticated():
            now = datetime.datetime.now()
            country = current_user.get_profile().country
            if country != None:
	            redis.Redis().set(current_user.username, {"country_name": country.name, "country_id": country.id})
	            redis.Redis().expire(current_user.username, settings.USER_LASTSEEN_TIMEOUT)