from django.conf.urls import url
from . import views


urlpatterns = [
   #url(r'^$', views.personel_new, name='post_list'),
    url(r'^parser/$', views.frame, name='parser'),
    url(r'^personel/new/$', views.personel_new, name='personel_new'),
    url(r'^new/dte/$', views.new_dte, name='new_dte'),
    url(r'^new/dte/work_list$', views.get_work, name='work_list'),
    url(r'^dtes/$', views.dte_list, name='dte_list'),
    url(r'^dte/(?P<nn>[0-9]+)/edit/$', views.dte_edit, name='dte_edit'),

]