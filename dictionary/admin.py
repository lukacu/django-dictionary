# -*- Mode: python; indent-tabs-mode: nil; c-basic-offset: 2; tab-width: 2 -*- 
from dictionary.models import Phrase, Translation
from django.contrib import admin

class PhraseAdmin(admin.ModelAdmin):
    # ...
    list_display = ('content', 'user', 'created')

class TranslationAdmin(admin.ModelAdmin):
    # ...
    list_display = ('content', 'user', 'phrase', 'created')


admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Translation, TranslationAdmin)
