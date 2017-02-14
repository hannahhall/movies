from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
import json
from v1 import guidebox


class IndexView(TemplateView):
    template_name = 'search_app/index.html'


def search_by_title(request):
    name = request.POST['movie_name']
    movie_list = guidebox.Search().movie_search_by_title(
        field='title',
        query=name
    )
    return HttpResponse(movie_list, content='application/json')

def movie_detail(request, movie_id):
    detail = guidebox.Search().movie_lookup_by_id(movie_id)
    cast = detail['cast'][:5]
    movie_list = guidebox.Search().find_related_movies(movie_id)
    return HttpResponse([detail, cast, movie_list], content='application/json')

def search_by_actor(request):
    name = request.POST['actor_name']
    actor_list = guidebox.Search().search_for_actor(name)
    return HttpResponse(actor_list, content='application/json')

def actor_detail(request, actor_id):
    actor_id = request.POST['actor_id']
    actor = guidebox.Search().actor_lookup_by_id(actor_id)
    credits = guidebox.Search().retrieve_actor_credits(actor_id)
    return HttpResponse([actor, credits], content='application/json')
