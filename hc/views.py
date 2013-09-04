from hc.models import Country
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.utils.translation import ugettext as _
from hc.activeuser_middleware import get_online_users
from django.contrib.auth.decorators import login_required

# frontpage of HC
def home(request):    
	return render_to_response("main.html", {"online_users": get_online_users()}, context_instance=RequestContext(request))

# users own profile 
@login_required
def profile(request):
	return render_to_response("registration/profile.html", context_instance=RequestContext(request))

# faq page
def faq(request):    
	return render_to_response("faq.html", context_instance=RequestContext(request))

# learn page
def learn(request):    
	return render_to_response("learn.html", context_instance=RequestContext(request))

# rules page
def rules(request):    
	return render_to_response("rules.html", context_instance=RequestContext(request))

# tour pages
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

# about page
def about(request):    
    return render_to_response("about.html", context_instance=RequestContext(request))

# countries page
def countries(request):
	countries = Country.objects.all().order_by("name")
	return render_to_response("countries.html", {"countries": countries}, context_instance=RequestContext(request))

# country page
def country(request, id):
	country = Country.objects.get(id = id)
	return render_to_response("country.html", {"country": country}, context_instance=RequestContext(request))
