from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'test_project.views.demo'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
         'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )
