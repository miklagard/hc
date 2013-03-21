# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models.signals import post_save
import datetime
from hc.settings import USER_ONLINE_TIMEOUT, UPLOAD_DIR
import redis
from easy_thumbnails.fields import ThumbnailerImageField

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

	picture = ThumbnailerImageField(upload_to=UPLOAD_DIR, blank=True)
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

	#registration_date = models.DateField(default=datetime.datetime.now())
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

	comments =  models.ForeignKey("Comments", null=True, blank=True)

	def member_since(self):
		from dateutil import relativedelta as rdelta
		from datetime import datetime
		rd = rdelta.relativedelta(datetime.now(), self.user.date_joined)
		return "{0.years} years, {0.months} months {0.days} days".format(rd)

	def notifications(self):
		ret = []
		if self.should_notify:
			ret.append("should notify %s days in advance" % str(self.should_notify))

		if self.can_call_on_arrival == True:
			ret.append("can call on arrival")

		if self.call_from == "" and self.call_to != "":
			ret.append("asked to call before %s" % self.call_to)

		if self.call_from != "" and self.call_to == "":
			ret.append("asked to call after %s" % selfcall_from)

		if self.call_from != "" and self.call_to != "":
			ret.append("asked to call between %s and %s" % (self.call_from, self.call_to))

		return ", ".join(ret)

	def pleasebring(self):
		ret = []
		if self.bring_tent:
			ret.append("tent")
		if self.bring_camping_mattress:
			ret.append("mattress") 
		if self.bring_sleeping_bag:
			ret.append("sleeping bag")
		return ", ".join(ret)

	def sleeping_offer(self):
		ret = []
		if self.offer_garden:
			ret.append("garden")
		if self.offer_sofa:
			ret.append("sofa")
		if self.offer_sperate_room:
			ret.append("separated room")
		if self.offer_floor:
			ret.append("floor")
		if self.offer_mattress:
			ret.append("mattress")
		if self.offer_bed:
			ret.append("bed")
		if self.offer_other:
			ret.append(self.offer_other)
		return ", ".join(ret)

	def i_offer(self):
		ret = []
		if self.offer_dinner:
			ret.append("have someone over for dinner")
		if self.show_around_town:
			ret.append("show around town")
		if self.icanoffer:
			ret.append(self.icanoffer)

		return ", ".join(ret)

	def instant_contact(self):
		ret = []
		if self.icq != "":
			ret.append({"what": "ICQ", "value": self.icq})
		if self.skype != "":
			ret.append({"what": "Skype", "value": self.skype})
		if self.aol != "":
			ret.append({"what": "AOL", "value": self.aol})
		if self.yahoo != "":
			ret.append({"what": "Yahoo Messenger", "value": self.yahoo})
		if self.other_chat != "":
			ret.append({"what": "Others", "value": self.other_chat})
		return ret

	def restrictions(self):
		ret = []
		if self.restrictions_no_drugs:
			ret.append("no drugs")
		if self.restrictions_no_alcohol:
			ret.append("no alcohol")
		if self.restrictions_no_dishes:
			ret.append("no dishes")
		if self.restrictions_pay_for_phone_calls:
			ret.append("has to pay for phone calls")
		if self.restrictions_pay_for_food:
			ret.append("has to pay for food")
		if self.restrictions_other != "":
			ret.append(self.restrictions_other)
		return ", ".join(ret)

	def gender_desc(self):
		if self.gender == "f":
			return "Female"
		elif self.gender == "m":
			return "Male"
		else:
			return ""

	def live_with(self):
		ret = []
		if self.live_with_partner:
			ret.append("my partner (wife, husband, girl/boyfriend)")
		if self.live_with_parents:
			ret.append("parents")
		if self.live_with_other_people:
			ret.append("other people")
		if self.live_with_my_children:
			ret.append("my child(ren)")
		if self.live_with_siblings:
			ret.append("siblings")
		if self.live_alone:
			ret.append("alone")

		return ", ".join(ret)

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

class Comments(models.Model):
	comment_created = models.DateField(null=False, blank=False, default=datetime.datetime.now())
	comment_updated = models.DateField(null=False, blank=False, default=datetime.datetime.now())

	trust = models.BooleanField(default=False)
	host = models.BooleanField(default=False)
	guest = models.BooleanField(default=False)
	passport_checked = models.BooleanField(default=False)
	where_did_you_meet = models.CharField(max_length=300, null=False, blank=False)
	comment = models.CharField(max_length=500, null=False, blank=False)

	user = models.ForeignKey(User) 

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: u.get_profile())