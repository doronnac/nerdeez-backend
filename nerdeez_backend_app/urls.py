'''
Created on May 20, 2013
will create the views for the server app
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.contrib import admin
from tastypie.api import Api
from nerdeez_backend_app.nerdeez_api.api import UniversityResource
import nerdeez_backend_app.views

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(UniversityResource())

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin URLs
#===============================================================================

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nerdeez_backend_app.views.home', name='home'),
    # url(r'^nerdeez_backend_app/', include('nerdeez_backend_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^api/', include(v1_api.urls)),
    ('^$', nerdeez_backend_app.views.porthole),
    (r'^search/', include('haystack.urls')),
    #('^proxy/', nerdeez_backend_app.views.proxy),
)

#if not settings.DEBUG:    
urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                        )

#===============================================================================
# end URLs
#===============================================================================