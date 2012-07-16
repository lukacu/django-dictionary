# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from django import forms
from django.forms import widgets
from django.db import transaction, models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from datetime import datetime
from dictionary.models import Phrase, Translation

class PhraseForm(forms.ModelForm):
  class Meta:
    model = Phrase
    exclude = ('user',)

  def __init__(self, user, *args, **kwargs):
    self._user = user
    super(PhraseForm, self).__init__(*args, **kwargs)

  def save(self, commit=True):
    inst = super(PhraseForm, self).save(commit=False)
    inst.user = self._user
    if commit:
      inst.save()
    return inst


class TranslationForm(forms.ModelForm):
  class Meta:
    model = Translation
    exclude = ('user', 'phrase')

  def __init__(self, user, phrase, *args, **kwargs):
    self._user = user
    self._phrase = phrase
    super(TranslationForm, self).__init__(*args, **kwargs)

  def save(self, commit=True):
    inst = super(TranslationForm, self).save(commit=False)
    inst.user = self._user
    inst.phrase = self._phrase
    if commit:
      inst.save()
    return inst
