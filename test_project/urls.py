from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'test_project.views.gallery'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
        # (r'^404-error-page/$', direct_to_template, {'template': '404.html'}),
        # (r'^500-error-page/$', direct_to_template, {'template': '500.html'}),
    )
