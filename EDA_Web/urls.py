from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'EDA_Web.views.home', name='home'),
    url(r'^about/', 'EDA_Web.views.about', name='about'),
    url(r'^achievement/', 'EDA_Web.views.achievement', name='achievement'),
    url(r'^activity/', 'EDA_Web.views.activity', name='activity'),
    url(r'^contact/', 'EDA_Web.views.contact', name='contact'),
    url(r'^downloads/', 'EDA_Web.views.downloads', name='downloads'),
    url(r'^feeds/', 'EDA_Web.views.feeds', name='feeds'),
    url(r'^members/', 'EDA_Web.views.members', name='members'),
    url(r'^news/', 'EDA_Web.views.news', name='news'),
    url(r'^admin/', include(admin.site.urls)),
)