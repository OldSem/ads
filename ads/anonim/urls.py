# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ads_list, name='ads_list'),
    url(r'^new_ad/$', views.new_ad, name='new_ad'),
    url(r'^ads_filter/(?P<teg>[0-9]+)/(?P<activ>[1-2])/(?P<b_date>)/(?P<e_date>)/(?P<text>)/$', views.ads_filter, name='ads_filter'),
    #url(r'^new/dte/$', views.new_dte, name='new_dte'),
    #url(r'^new/dte/work_list$', views.get_work, name='work_list'),
    #url(r'^dtes/$', views.dte_list, name='dte_list'),
    #url(r'^dte/(?P<nn>[0-9]+)/edit/$', views.dte_edit, name='dte_edit'),

]