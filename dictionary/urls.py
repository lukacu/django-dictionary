# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from django.conf.urls.defaults import *

urlpatterns = patterns('',
  url(r'^$', 'dictionary.views.phrases', name='dictionary-list'),
  url(r'^(?P<phrase>\d+)(?:/.*)?$', 'dictionary.views.phrase', name='dictionary-phrase'),
  url(r'^ask/$', 'dictionary.views.new_phrase', name='dictionary-ask'),
  url(r'^translate/(?P<phrase>\d+)$', 'dictionary.views.add_translation', name='dictionary-translate'),
  url(r'^vote/(?P<translation>\d+)$', 'dictionary.views.vote_translation', name='dictionary-vote'),
  url(r'^delete/(?P<phrase>\d+)$', 'dictionary.views.delete_phrase', name='dictionary-delete'),
  url(r'^untranslate/(?P<translation>\d+)$', 'dictionary.views.remove_translation', name='dictionary-untranslate'),
)
