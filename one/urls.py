from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^show/(?P<show_str>.+)$', views.show, name='show'),
]