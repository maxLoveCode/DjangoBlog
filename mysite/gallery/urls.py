from django.conf.urls import include, url
import gallery.views


__author__ = 'Max'


urlpatterns = [
    url(r'^$', gallery.views.index),
]
