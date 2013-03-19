from django.db import models
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 36)

    def __unicode__(self):
        return u"%s" % self.name

class UserProfile(models.Model):
	GENDER_CHOICES=(('m', 'Male'), ('f', 'Female'))
	
	fullname = models.CharField(max_length=50, null=False, blank=False)
	street = models.CharField(max_length=300)
	country = models.ForeignKey("Country")

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	birth_date = models.DateField()
	phone_home = models.CharField(max_length=12)
	phone_work  = models.CharField(max_length=12)
	fax = models.CharField(max_length=12)
	occupation = models.CharField(max_length=20)
	profile_summary = models.TextField()

	icq = models.CharField(max_length=12, null=True, blank=True)
	skype = models.CharField(max_length=22, null=True, blank=True)
	aol = models.CharField(max_length=12, null=True, blank=True)
	yahoo = models.CharField(max_length=12, null=True, blank=True)
	other_chat = models.CharField(max_length=50, null=True, blank=True)