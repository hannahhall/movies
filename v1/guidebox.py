import guidebox
from .api_key import key



class Search:

    guidebox.api_key = key

    def movie_search_by_title (self, field, query):
        """Search for movies by title"""
        results = guidebox.Search.movies(field=field, query=query)
        return results.results

    def movie_lookup_by_id(self, movie_id):
        """Look up specific movie by id"""
        result = guidebox.Movie.retrieve(id=movie_id)
        return result
