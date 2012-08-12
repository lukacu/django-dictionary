from django.db.models.aggregates import Count
from dictionary.models import Translation, Phrase

__author__ = 'lukacu'

from django.template import Library, Node, TemplateSyntaxError
from django.utils.translation import ugettext as _

register = Library()

class RecentTranslationsNode(Node):
    def __init__(self, context_var):
        self.context_var = context_var

    def render(self, context):
        context[self.context_var] = Translation.objects.all().order_by('created')[0:5]
        return ''

class UntranslatedNode(Node):
    def __init__(self, context_var):
        self.context_var = context_var

    def render(self, context):
        context[self.context_var] = Phrase.objects.annotate(translation_count = Count('translation')).filter(translation_count__eq = 0).order_by('-created')
        return ''

def do_recent_translations(parser, token):
    """
    {% recent_translations as [varname] %}
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError(_('%s requires exactly two arguments') % bits[0])
    if bits[1] != 'as':
        raise TemplateSyntaxError(_("second argument to %s must be 'as'") % bits[0])
    return RecentTranslationsNode(bits[2])

def do_untranslated(parser, token):
    """
    {% recent_translations as [varname] %}
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError(_('%s requires exactly two arguments') % bits[0])
    if bits[1] != 'as':
        raise TemplateSyntaxError(_("second argument to %s must be 'as'") % bits[0])
    return UntranslatedNode(bits[2])


register.tag('recent_translations', do_recent_translations)
register.tag('untranslated', do_untranslated)

