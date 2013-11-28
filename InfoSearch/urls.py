from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InfoSearch.views.home', name='home'),
    # url(r'^InfoSearch/', include('InfoSearch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ('^$', index),
    ('^index/$', index),
    ('^admin/$', admin),
    ('^admin_add/$', admin_add),
    ('^admin_del/$', admin_del),
    ('^add/$', add),
    ('^add_action/$', add_action),
    ('^search/$', search),
    ('^login/$', login),
    ('^logout/$', logout),
    ('^del_data/$', del_data),
    ('^update/$', update),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# This will work if DEBUG is True
urlpatterns += staticfiles_urlpatterns()