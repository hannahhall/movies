from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
import json
from v1 import guidebox

class IndexView(TemplateView):
    template_name = 'search_app/index.html'

def search(request):
    name = request.POST['movie_name']
    movie_list = guidebox.Search().movie_search_by_title(
        field='title',
        query=name
    )
    return render(
        request,
        'search_app/movie_list.html',
        {'movie_list': movie_list}
    )

def movie_detail(request, movie_id):
    detail = guidebox.Search().movie_lookup_by_id(movie_id=movie_id)
    cast = detail['cast'][:5]
    return render(
        request,
        'search_app/movie_detail.html',
        {'detail': detail, 'cast':cast}
    )
