from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'dictionary.views.phrases'),
  url(r'^dictionary/', include('dictionary.urls')),
  (r'^comments/', include('django.contrib.comments.urls')),
  (r'^user/', include('django_openid_auth.urls')),
  url(r'^user/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
  (r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

static_patterns = patterns('',
url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

media_url = settings.MEDIA_URL.lstrip('/')
urlpatterns += patterns('',
(r'^%s' % media_url, include(static_patterns)),
)
