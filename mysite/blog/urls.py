from django.conf.urls import include, url
import blog.views


__author__ = 'Max'


urlpatterns = [
    url(r'^$', blog.views.index),
    url(r'^tags/', blog.views.index),
    url(r'(?P<slug>[\w-]+)/$$', blog.views.detail),
]
