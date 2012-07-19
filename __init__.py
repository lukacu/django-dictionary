# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from django.contrib.comments.views import comments
from django.http import HttpResponseRedirect, HttpResponse

original_post_comment = comments.post_comment
def post_comment(request, next=None):
  if not request.user.is_authenticated():
    from django.template.loader import render_to_string
    from django import http
    response = HttpResponse()
    response.status_code = 401  
    return response
  return original_post_comment(request, next)

comments.post_comment = post_comment
