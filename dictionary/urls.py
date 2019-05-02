# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*-
from django.conf.urls import *

from dictionary.views import phrases, phrase, search, new_phrase, add_translation, vote_translation, delete_phrase, remove_translation

urlpatterns = [
  url(r'^$', phrases, name='dictionary-list'),
  url(r'^search/.*', search, name='dictionary-search'),
  url(r'^phrase/(?P<phrase>\d+)(?:/.*)?$', phrase, name='dictionary-phrase'),
  url(r'^ask/$', new_phrase, name='dictionary-ask'),
  url(r'^translate/(?P<phrase>\d+)$', add_translation, name='dictionary-translate'),
  url(r'^vote/(?P<translation>\d+)$', vote_translation, name='dictionary-vote'),
  url(r'^delete/(?P<phrase>\d+)$', delete_phrase, name='dictionary-delete'),
  url(r'^untranslate/(?P<translation>\d+)$', remove_translation, name='dictionary-untranslate'),
]

