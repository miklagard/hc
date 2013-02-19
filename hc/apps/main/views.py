#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

def main(request):
	return HttpResponse("here we go")