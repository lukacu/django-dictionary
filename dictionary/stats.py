# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from dictionary.models import Phrase, Translation
from django.db.models import Count
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader

def stats_active_users():
  return

