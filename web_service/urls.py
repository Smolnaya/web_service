from django.conf.urls import url
from django.views.generic import TemplateView

from web_service.articles import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^article/$', views.article_list, name='article_list'),
    url(r'^article/create/$', views.article_create, name='article_create'),
    url(r'^article/(?P<pk>\d+)/open/$', views.article_open, name='article_open'),
    url(r'^article/(?P<pk>\d+)/update/$', views.article_update, name='article_update'),
    url(r'^article/(?P<pk>\d+)/delete/$', views.article_delete, name='article_delete'),
    url(r'search_articles', views.search_articles, name='search_articles'),
    url(r'get_authors', views.get_authors, name='get_authors'),
    url(r'get_source', views.get_source, name='get_source'),
]
