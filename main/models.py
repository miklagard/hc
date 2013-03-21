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
	GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
	GENDER_OF_GUEST = (("Male", "Male"), ("Female", "Female"), ("Doesn't Matter", "Doesn't Matter"))
	ACCOMODATION_OFFER = ("Yes", "Yes"), ("Maybe", "Maybe"), ("No", "No, Please Don't Ask")
	NUMBER_OF_GUEST = ((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10, 10))
	SMOKING = (("No Problem", "No Problem"), ("Outside Only", "Outside Only"), ("Not At All", "Not At All"))
	fullname = models.CharField(max_length=50, null=True, blank=True)
	street = models.CharField(max_length=300, null=True, blank=True)
	country = models.ForeignKey("Country", null=True, blank=True)
	postal_code = models.CharField(max_length=6, null=True, blank=True)

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

	languages_spoken = models.CharField(max_length=100, null=True, blank=True)
	hobbies_interests = models.CharField(max_length=300, null=True, blank=True)
	organizations = models.CharField(max_length=200, null=True, blank=True)
	travel_experience = models.CharField(max_length=500, null=True, blank=True)
	planned_trips = models.CharField(max_length=500, null=True, blank=True)
	anything_else = models.CharField(max_length=300, null=True, blank=True)
	offer_accomodation = models.CharField(max_length=5, choices=ACCOMODATION_OFFER, null=True, blank=True)
	best_times = models.CharField(max_length=300, null=True, blank=True)
	icanoffer = models.CharField(max_length=200, null=True, blank=True)
	offer_dinner = models.BooleanField(default=False)
	show_around_town = models.BooleanField(default=False)
	nearbytransport = models.CharField(max_length=300, null=True, blank=True)
	nearbycities = models.CharField(max_length=500, null=True, blank=True)
	interestingthings = models.CharField(max_length=500, null=True, blank=True)

	gender_of_guest = models.CharField(choices=GENDER_OF_GUEST, max_length=14, null=True, blank=True, default="Doesn't Matter")
	number_of_guest = models.IntegerField(choices=NUMBER_OF_GUEST, null=True, blank=True)

	live_with_partner = models.BooleanField(default=False)
	live_with_parents = models.BooleanField(default=False)
	live_with_other_people = models.BooleanField(default=False)
	live_with_my_children = models.BooleanField(default=False)
	live_with_siblings = models.BooleanField(default=False)
	live_alone = models.BooleanField(default=False)

	bring_tent = models.BooleanField(default=False)
	bring_camping_mattress = models.BooleanField(default=False)
	bring_sleeping_bag = models.BooleanField(default=False)

	offer_garden = models.BooleanField(default=False)
	offer_sofa = models.BooleanField(default=False)
	offer_sperate_room = models.BooleanField(default=False)
	offer_floor = models.BooleanField(default=False)
	offer_mattress = models.BooleanField(default=False)
	offer_bed = models.BooleanField(default=False)
	offer_other = models.CharField(max_length=30, null=True, blank=True)

	last_login = models.DateField(default=datetime.datetime.now())
	registration_date = models.DateField(default=datetime.datetime.now())
	last_update = models.DateField(default=datetime.datetime.now())

	restrictions_no_drugs = models.BooleanField(default=False)
	restrictions_no_alcohol = models.BooleanField(default=False)
	restrictions_no_dishes = models.BooleanField(default=False)
	restrictions_pay_for_phone_calls = models.BooleanField(default=False)
	restrictions_pay_for_food = models.BooleanField(default=False)
	restrictions_other = models.CharField(max_length=50, null=True, blank=True)
	
	should_notify = models.IntegerField(null=True, blank=True)
	can_call_on_arrival = models.BooleanField(default=False)

	smoking = models.CharField(choices=SMOKING, max_length=12, null=True, blank=True, default="Outside Only")

	maximum_days_of_stay = models.CharField(max_length=50, null=True, blank=True)

	call_from = models.CharField(max_length=5, null=True, blank=True)
	call_to = models.CharField(max_length=5, null=True, blank=True)

	pets = models.CharField(max_length=50, null=True, blank=True)

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