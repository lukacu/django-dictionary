# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*-
from django import forms
from django.forms import widgets
from django.db import transaction, models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from datetime import datetime
from dictionary.models import Phrase, Translation


class SearchForm(forms.Form):

  query = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': _('Enter search query')}))

class PhraseForm(forms.ModelForm):
  class Meta:
    model = Phrase
    exclude = ('user', 'description')
    widgets = {
        'content': forms.TextInput({ "placeholder": _("Enter a new phrase")}),
        }

  def __init__(self, user, *args, **kwargs):
    self._user = user
    super(PhraseForm, self).__init__(*args, **kwargs)

  def save(self, commit=True):
    inst = super(PhraseForm, self).save(commit=False)
    inst.user = self._user
    if commit:
      inst.save()
    return inst

class PhraseDescriptionForm(forms.Form):

  description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Describe the phrase')}))


class TranslationForm(forms.ModelForm):
  class Meta:
    model = Translation
    exclude = ('user', 'phrase')
    widgets = {
          'content': forms.TextInput({ "placeholder": _("Recommend a translation")}),
    }

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
