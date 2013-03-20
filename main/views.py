# -*- coding:utf-8 -*-
from hc.main.models import Country, UserProfile
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.utils.translation import ugettext as _
from django.contrib import auth
from django.contrib.auth.models import User
from hc.main.forms import ProfileForm
import redis

def online_users():
	ret = []
	for k in redis.Redis().keys():
		ret.append(k)
	return ret

def home(request):    
    return render_to_response("main.html", {"online": online_users()}, context_instance=RequestContext(request))

def faq(request):    
    return render_to_response("faq.html", context_instance=RequestContext(request))

def learn(request):    
    return render_to_response("learn.html", context_instance=RequestContext(request))

def stopspam(request):    
    return render_to_response("stopspam.html", context_instance=RequestContext(request))

def spammerfame(request):    
    return render_to_response("spammerfame.html", context_instance=RequestContext(request))

def rules(request):    
    return render_to_response("rules.html", context_instance=RequestContext(request))

def edit(request):    
    if request.method == 'POST': 
        form = ProfileForm(request.POST, instance=request.user.get_profile()) 
        if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/profile/') 
    else:
        form = ProfileForm(instance=request.user.get_profile()) 

    return render_to_response("edit.html", {"form": form}, context_instance=RequestContext(request))

def userprofile(request, username):
	profile = get_object_or_404(UserProfile, user=get_object_or_404(User, username=username))
	return render_to_response("userprofile.html", {"user": profile}, context_instance=RequestContext(request))

def tour(request, nr):
	if int(nr) == 1:
		return render_to_response("tour1.html", context_instance=RequestContext(request))
	elif int(nr) == 2:
		return render_to_response("tour2.html", context_instance=RequestContext(request))
	elif int(nr) == 3:
		return render_to_response("tour3.html", context_instance=RequestContext(request))
	elif int(nr) == 4:
		return render_to_response("tour4.html", context_instance=RequestContext(request))
	elif int(nr) == 5:
		return render_to_response("tour5.html", context_instance=RequestContext(request))
	elif int(nr) == 6:
		return render_to_response("tour6.html", context_instance=RequestContext(request))

def about(request):    
    return render_to_response("about.html", context_instance=RequestContext(request))

def countries(request):
	countries = Country.objects.all().order_by("name")
	return render_to_response("countries.html", {"countries": countries}, context_instance=RequestContext(request))

def country(request, id):
	country = Country.objects.get(id = id)
	return render_to_response("country.html", {"country": country}, context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return render_to_response("main.html", {"online": online_users()}, context_instance=RequestContext(request))

#@login_required
def profile(request):
	return render_to_response("profile.html", {"usr": request.user.get_profile()}, context_instance=RequestContext(request))
