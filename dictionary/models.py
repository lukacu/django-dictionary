# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Phrase(models.Model):
    user = models.ForeignKey(User, null = True)
    content = models.CharField(_('phrase'), max_length = 255, blank = False, unique = True)
    created = models.DateTimeField(auto_now_add = True, editable = False)
    modified = models.DateTimeField(auto_now = True, editable = False)
    description = models.TextField(_('description'), blank = True, unique = False)

    def first_letter(self):
        return self.content and self.content[0].lower() or ''

    def __unicode__(self):
        return self.content

class Translation(models.Model):
    phrase = models.ForeignKey(Phrase)
    user = models.ForeignKey(User, null = True)
    content = models.CharField(_('translation'), max_length = 255, blank = False)
    created = models.DateTimeField(auto_now_add = True, editable = False)

    class Meta:
        unique_together = ("phrase", "content")

    def first_letter(self):
        return self.content and self.content[0].lower() or ''

    def is_approved(self):
      try:
          return (self.approval is not None)
      except Approval.DoesNotExist:
          return False

    def __unicode__(self):
        return self.content

class Vote(models.Model):
    translation = models.ForeignKey(Translation)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True, editable = False)

    class Meta:
        unique_together = ("translation", "user")

    def __unicode__(self):
        return "User '%s' voted for '%s' translation of '%s'" % (self.user, self.translation, self.translation.phrase)

class Approval(models.Model):
    translation = models.OneToOneField(Translation)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True, editable = False)

    def __unicode__(self):
        return "Approval of '%s' translation of '%s' by user '%s'" % (self.translation, self.translation.phrase, self.user)

