# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models.signals import post_save
import datetime
from hc.settings import USER_ONLINE_TIMEOUT
import redis

class Country(models.Model):
    name = models.CharField(max_length = 36)

    def __unicode__(self):
        return u"%s" % self.name

class UserProfile(models.Model):
	GENDER_CHOICES=(('m', 'Male'), ('f', 'Female'))

	fullname = models.CharField(max_length=50, null=True, blank=True)
	street = models.CharField(max_length=300, null=True, blank=True)
	country = models.ForeignKey("Country", null=True, blank=True)

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	phone_home = models.CharField(max_length=12, null=True, blank=True)
	phone_work  = models.CharField(max_length=12, null=True, blank=True)
	fax = models.CharField(max_length=12, null=True, blank=True)
	occupation = models.CharField(max_length=20, null=True, blank=True)
	profile_summary = models.TextField(null=True, blank=True)

	icq = models.CharField(max_length=12, null=True, blank=True)
	skype = models.CharField(max_length=22, null=True, blank=True)
	aol = models.CharField(max_length=12, null=True, blank=True)
	yahoo = models.CharField(max_length=12, null=True, blank=True)
	other_chat = models.CharField(max_length=50, null=True, blank=True)

	user = models.OneToOneField(User) 
	
	def last_seen(self):
		return redis.Redis().get(self.user.username)

	def online(self):

		if redis.Redis().get(self.user.username):
			return True
		else:
			return False

	def __unicode__(self):
		return self.user.username
	
	class Meta:
		ordering=['-id']

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: u.get_profile())