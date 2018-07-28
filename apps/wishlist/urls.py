from django.conf.urls import url
from . import views     


urlpatterns = [
  url(r'^$', views.homepage),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^dashboard$', views.dashboard),
  url(r'^logout$', views.logout),
  url(r'^wish$', views.wish),
  url(r'^create_wish$', views.create_wish),
  url(r'^wish_item/(?P<id>\d+)$', views.wish_item),
  url(r'^wish_item_remove/(?P<id>\d+)$', views.remove_wish),
  url(r'^wish_item_add/(?P<id>\d+)$', views.add_wish_list),
]