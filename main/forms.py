#-*- coding: utf-8 -*-

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField, NullBooleanField, URLField, EmailField, IntegerField, ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, Select, Textarea
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from hc.main.models import *
import datetime

class ProfileForm(forms.ModelForm):
	this_year = datetime.date.today().year
	GENDER_CHOICES=(('m', 'Male'), ('f', 'Female'))
	GENDER_OF_GUEST=(("Male", "Male"), ("Female", "Female"), ("Doesn't Matter", "Doesn't Matter"))

	country = forms.ModelChoiceField(queryset=Country.objects.all().order_by("name"), label=u"Country", widget=Select(), required=False)   
	birth_date = forms.DateField(label="Birth Date", widget=SelectDateWidget(years=range(this_year-100, this_year-18)), required=True)

	class Meta:
		model = UserProfile
		exclude=("user","last_login","registration_date","last_update")