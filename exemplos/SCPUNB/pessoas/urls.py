from django.conf.urls import url
from .views import index_view, list_view, detail_view

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^all/$', list_view, name='list'),
    url(r'^(?P<id>[0-9]+)/$', detail_view, name='detail'),
]
