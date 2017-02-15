from django.conf.urls import url
from . import views

app_name = 'search_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^movie-search/$', views.search_by_title, name='movie_search'),
    url(r'^movie/(?P<movie_id>[0-9]+)/', views.movie_detail, name='detail'),
    url(r'^actor/(?P<actor_id>[0-9]+)/', views.actor_detail, name='actor_detail'),
    url(r'^actor-search/$', views.search_by_actor, name='actor_search')
]
