# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*-
from django.db.models import Count
from django.db import IntegrityError
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages

from django.http import Http404, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from dictionary.models import Phrase, Translation, Vote
from dictionary.forms import PhraseForm, TranslationForm, SearchForm

from django.db.models import Q

from django.utils.translation import ugettext as _

def overview(request):
  return render(request, 'dictionary/overview.html', {} )

def phrases(request):
  phrase_list = Phrase.objects.extra(select={'lower_content': 'lower(dictionary_phrase.content)'}).order_by('lower_content').annotate(translation_count = Count('translation'))

  return render(request, 'dictionary/list.html',
    { 'phrases' : phrase_list, 'form' : PhraseForm(request.user) })

def phrase(request, phrase):

  phrase = get_object_or_404(Phrase, id = int(phrase))
  translations = Translation.objects.filter(phrase = phrase.id).annotate(vote_count = Count('vote')).order_by('-vote_count')

  voted_for = None
  if request.user.is_authenticated():
    try:
      vote = Vote.objects.get(translation__phrase = phrase, user = request.user)
      voted_for = vote.translation
    except ObjectDoesNotExist:
      pass

  return render(request, 'dictionary/phrase.html',
    { 'phrase' : phrase, 'translations' : translations, 'voted' : voted_for, 'form' : TranslationForm(request.user, phrase) })

def search(request):

  results_phrase = None
  results_translation = None
  form = SearchForm()

  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      query = form.cleaned_data["query"]
      tags = [Q(content__icontains = tag) for tag in query.split(" ") if len(tag) > 0]

      if len(tags) > 0:

        query = tags.pop()
        for tag in tags:
            query &= tag

        results_phrase = Phrase.objects.extra(select={'lower_content': 'lower(dictionary_phrase.content)'}).filter(query).order_by('lower_content')

        results_translation = Translation.objects.extra(select={'lower_content': 'lower(dictionary_translation.content)'}).filter(query).order_by('lower_content')

  return render(request, 'dictionary/search.html', {'form': form, 'results_phrase' : results_phrase, 'results_translation' : results_translation} )


@login_required
def new_phrase(request):

  if request.method == 'POST':
    form = PhraseForm(request.user, request.POST)
    if form.is_valid():
      phrase = form.save()
      if phrase:
        messages.add_message(request, messages.INFO, _('Phrase added'))
        return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))
  else:
    form = PhraseForm(request.user)

  return render(request, 'dictionary/new.html', { 'form' : form })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_phrase(request, phrase):
  phrase = get_object_or_404(Phrase, id = int(phrase))

  phrase.delete()

  messages.add_message(request, messages.INFO, _('Phrase deleted'))

  return HttpResponseRedirect(reverse("dictionary-list"))


@login_required
def add_translation(request, phrase):

  phrase = get_object_or_404(Phrase, id = int(phrase))

  try:
    if request.method == 'POST':
      form = TranslationForm(request.user, phrase, request.POST)
      if form.is_valid() and form.save():
        messages.add_message(request, messages.INFO, _('Translation added'))
        return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))
    else:
      form = TranslationForm(request.user, phrase)
  except IntegrityError:
    pass

  return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def remove_translation(request, translation):
  translation = get_object_or_404(Translation, id = int(translation))

  phrase = translation.phrase.pk

  translation.delete()

  messages.add_message(request, messages.INFO, _('Translation deleted'))

  return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase)))


@login_required
def vote_translation(request, translation):

  translation = get_object_or_404(Translation, id = int(translation))
  vote = None

  try:
    vote = Vote.objects.get(translation__phrase = translation.phrase, user=request.user)
  except ObjectDoesNotExist:
    pass

  if vote:
    if vote.translation != translation:
      vote.delete()
      vote = Vote(user = request.user, translation = translation)
  else:
    vote = Vote(user = request.user, translation = translation)

  vote.save()

  return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = translation.phrase.pk)))

