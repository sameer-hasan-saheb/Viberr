from django.conf.urls import url
from .import views
import django.contrib.auth.views

app_name='music'

urlpatterns = [
    # music/
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$',views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

]
