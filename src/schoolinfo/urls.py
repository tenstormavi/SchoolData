from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'studentinfo.views.homepage', name='homepage'),
    url(r'^insert/$', 'studentinfo.views.home', name='insert'),
    url(r'^searchpage/$', 'studentinfo.views.searchpage', name='searchpage'),
    url(r'^search/$', 'studentinfo.views.search', name='search'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		                    document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
		                    document_root=settings.MEDIA_ROOT)