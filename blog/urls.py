from django.conf.urls import url
from . import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', blog_views.post_detail, name='post_detail'),
    url(r'^post/new/$', blog_views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', blog_views.post_edit, name='post_edit'),
]
