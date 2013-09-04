from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
	if pattern == "/":
		if request.path == pattern:
			return "active"
	elif request.path.startswith(pattern):
		return 'active'
	return ''
