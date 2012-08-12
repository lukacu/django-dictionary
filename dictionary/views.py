# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from django.db.models import Count
from django.db import IntegrityError
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from dictionary.models import Phrase, Translation, Vote
from dictionary.forms import PhraseForm, TranslationForm

def overview(request):
  return render_to_response('dictionary/overview.html',
    {  },
    context_instance = RequestContext(request)
  )

def phrases(request):
  phrase_list = Phrase.objects.extra(select={'lower_content': 'lower(dictionary_phrase.content)'}).order_by('lower_content').annotate(translation_count = Count('translation'))
#  paginator = Paginator(phrase_list, 50)

#  try:
#      page = int(request.GET.get('page', '1'))
#  except ValueError:
#      page = 1

#  try:
#      phrases = paginator.page(page)
#  except (EmptyPage, InvalidPage):
#      phrases = paginator.page(paginator.num_pages)

  return render_to_response('dictionary/list.html',
    { 'phrases' : phrase_list, 'form' : PhraseForm(request.user) },
    context_instance = RequestContext(request)
  )

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

  return render_to_response('dictionary/phrase.html',
    { 'phrase' : phrase, 'translations' : translations, 'voted' : voted_for, 'form' : TranslationForm(request.user, phrase) },
    context_instance = RequestContext(request)
  )


@login_required
def new_phrase(request):

  if request.method == 'POST':
    form = PhraseForm(request.user, request.POST)
    if form.is_valid():
      phrase = form.save()
      if phrase:
        return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))
  else:
    form = PhraseForm(request.user)

  return render_to_response('dictionary/new.html',
    { 'form' : form }, context_instance = RequestContext(request)  )

@login_required
def delete_phrase(request):

  pass

@login_required
def add_translation(request, phrase):

  phrase = get_object_or_404(Phrase, id = int(phrase))

  try:
    if request.method == 'POST':
      form = TranslationForm(request.user, phrase, request.POST)
      if form.is_valid() and form.save():
        return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))
    else:
      form = TranslationForm(request.user, phrase)
  except IntegrityError:
    pass

  return HttpResponseRedirect(reverse("dictionary-phrase", kwargs = dict(phrase = phrase.pk)))

@login_required
def remove_translation(request, phrase):

  pass

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


def server_error(request, template_name='500.html'):
  """
  500 error handler.

  Templates: `500.html`
  Context:
      MEDIA_URL
          Path of static media (e.g. "media.example.org")
  """
  t = loader.get_template(template_name) # You need to create a 500.html template.
  return HttpResponseServerError(t.render(Context({
    'MEDIA_URL': settings.MEDIA_URL
  })))
