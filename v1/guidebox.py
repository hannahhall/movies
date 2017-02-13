import guidebox
from .api_key import key



class Search:

    guidebox.api_key = key

    def movie_search_by_title(self, field, query):
        """Search for movies by title"""
        results = guidebox.Search.movies(field=field, query=query)
        return results.results

    def find_related_movies(self, movie_id):
        results = guidebox.Movie.related(id=movie_id)
        return results.results

    def movie_lookup_by_id(self, movie_id):
        """Look up specific movie by id"""
        result = guidebox.Movie.retrieve(id=movie_id)
        return result

    def movie_search_by_tag(self, tag_name):
        results = guidebox.Movie.list(tag = tag_name)
        return results

    def search_for_actor(self, name):
        results = guidebox.Search.person(query=name)
        return results

    def actor_lookup_by_id(self, actor_id):
        person = guidebox.Person.retrieve(id=actor_id)
        return person

    def retrieve_actor_credits(self, actor_id):
        credits = guidebox.Person.credits(id=212668)
        return credits

    def retrieve_movies_user_prefered_services(self, *args):
        sources = ','.join(args) if len(args) > 1 else ''.join(args)
        results = guidebox.Movie.list(sources = sources)
        return results
