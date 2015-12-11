from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_main),
    url(r'^blog/$', views.post_list_main, name='front-page'),
    url(r'^blog/([0-9]+)/$', views.post_list, name='post-list'),
    url(r'^blog/about/$', views.about, name='about-page'),
    url(r'^blog/post/$', views.submit_post, name='post-new'),
]
