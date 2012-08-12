# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Phrase(models.Model):
  user = models.ForeignKey(User, null = True)
  content = models.CharField(_('phrase'), max_length = 255, blank = False, unique=True)
  created = models.DateTimeField(auto_now_add = True, editable = False)
  modified = models.DateTimeField(auto_now = True, editable = False) 

  def first_letter(self):
      return self.content and self.content[0].lower() or ''

class Translation(models.Model):
  phrase = models.ForeignKey(Phrase)
  user = models.ForeignKey(User, null = True)
  content = models.CharField(_('translation'), max_length = 255, blank = False)
  created = models.DateTimeField(auto_now_add = True, editable = False)

  class Meta:
    unique_together = ("phrase", "content")

  def first_letter(self):
      return self.content and self.content[0].lower() or ''


class Vote(models.Model):
  translation = models.ForeignKey(Translation)
  user = models.ForeignKey(User)
  created = models.DateTimeField(auto_now_add = True, editable = False)

  class Meta:
    unique_together = ("translation", "user")
