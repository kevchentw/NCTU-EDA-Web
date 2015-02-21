from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from EDA_Web.service import Service
from EDA_Web.service import NewsService

urlpatterns = patterns('',
                       url(r'^$', 'EDA_Web.views.home', name='home'),
                       url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       url(r'^about/', 'EDA_Web.views.about', name='about'),
                       url(r'^achievement/', 'EDA_Web.views.achievement', name='achievement'),
                       url(r'^activity/', 'EDA_Web.views.activity', name='activity'),
                       url(r'^contact/', 'EDA_Web.views.contact', name='contact'),
                       url(r'^downloads/', 'EDA_Web.views.downloads', name='downloads'),
                       url(r'^feeds/', 'EDA_Web.views.feeds', name='feeds'),
                       url(r'^members/', 'EDA_Web.views.members', name='members'),
                       url(r'^news/', 'EDA_Web.views.news', name='news'),
                       url(r'^kcw/', 'EDA_Web.views.kcw', name='kcw'),
                       url(r'^kcw_research/', 'EDA_Web.views.kcw_research', name='kcw_research'),
                       url(r'^tyho/', 'EDA_Web.views.tyho', name='tyho'),
                       url(r'^tyho_research/', 'EDA_Web.views.tyho_research', name='tyho'),
                       url(r'^ylli/', 'EDA_Web.views.ylli', name='ylli'),
                       url(r'^ylli_research/', 'EDA_Web.views.ylli_research', name='ylli'),
                       url(r'^reset/', 'EDA_Web.views.reset', name='reset'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^html/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': '/home/administrator/NCTU-EDA-Web/html', })
)
Service.News = NewsService()
