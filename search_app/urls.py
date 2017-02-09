from django.conf.urls import url
from . import views

app_name = 'search_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^movie/(?P<movie_id>[0-9]+)/', views.movie_detail, name='detail'),
    url(r'^related/(?P<movie_id>[0-9]+)/', views.related_movies, name='related')
]
