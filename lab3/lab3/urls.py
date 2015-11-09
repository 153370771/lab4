from django.conf.urls import patterns, include, url
from blog.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^delete/', delete),
    url(r'^update/', update),
    url(r'^search/', search),
    url(r'^sear/', sear),            
    url(r'^$', index),
    url(r'^add/', add),
    url(r'^addbook/', addbook),                
    url(r'^authoradd/', authoradd),
    url(r'^showall/', showall),
    url(r'^showdata/', showdata),
    url(r'^images/', images),
    url(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'g:/ms-project/lab3/images'}), 
)
