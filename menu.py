from movie_search import Search
import guidebox
import json
import itertools


class Menu:

    def __init__(self):
        self.search = Search()
        self.movie_list = []

    def menu(self):
        while True:
            if self.movie_list:
                self.print_movie_list()
            else:
                self.get_movie_list()

    def get_movie_list (self):
        title = input('What movie would you like to find? \n> ')
        results = self.search.movie_search_by_title(
            field='title',
            query = title
        )
        self.movie_list.extend(results)
        self.print_movie_list()

    def print_movie_list(self):
        counter = itertools.count(start=1)
        [print(
            '{0}: {1} {2}'.format(
                str(next(counter)),
                movie["original_title"],
                movie['release_year']
            ))
            for movie in self.movie_list]
        # print('{}: Find a different movie'.format(str(next(counter))))
        index = input('Choose which movie you want to watch \n> ')
        if int(index) == counter:
            self.get_movie_list()
        else:
            self.find_streaming_urls(index = int(index) - 1)

    def find_streaming_urls(self, index):
        guide_id = self.movie_list[index]["id"]
        result = self.search.movie_lookup_by_id(guide_id)
        if result['subscription_web_sources']:
            [print('{0}: {1}'
                .format(url['display_name'], url['link']))
                for url in result['subscription_web_sources']
            ]
        else:
            print('No subscription sources for this movie')



# "subscription_web_sources"

if __name__ == '__main__':
    Menu().menu()
