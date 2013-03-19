# Create your views here.

from hc.main.models import Country
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext

def home(request):    
    return render_to_response("main.html", context_instance=RequestContext(request))