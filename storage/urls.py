from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'storage.views.index'),
    url(r'^login/$', 'storage.views.login'),
    url(r'^logout/$', 'storage.views.logout'),
    
    url(r'^store/index/$', 'storage.views.store_index'),
    
    url(r'^store/stock/$', 'storage.views.store_stock'),
    
    url(r'^store/history/$', 'storage.views.store_history'),
    
    url(r'^store/calculate/$', 'storage.views.store_calculate'),
    
    url(r'^store/help/$', 'storage.views.store_help'),
    
    url(r'^store/account/$', 'storage.views.store_account'),
    url(r'^store/change_password/$', 'storage.views.store_change_password'),
    url(r'^store/change_email/$', 'storage.views.store_change_email'),
    
    url(r'^store/system/$', 'storage.views.store_system'),
    
    url(r'^store/data/$', 'storage.views.store_data'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)
