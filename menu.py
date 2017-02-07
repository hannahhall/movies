from movie_search import Search
import guidebox
import json
import itertools
import os

def pause(message='\nPress enter to continue.'):
    input(message)

def clear_menu():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Menu:

    def __init__(self):
        self.search = Search()
        self.movie_list = []

    def menu(self):
        while True:
            if self.movie_list:
                clear_menu()
                self.print_movie_list()
            else:
                clear_menu()
                self.get_movie_list()

    def get_movie_list (self):
        clear_menu()
        title = input('What movie would you like to find? \n> ')
        results = self.search.movie_search_by_title(
            field='title',
            query = title
        )
        self.movie_list = results
        self.print_movie_list()

    def print_movie_list(self):
        clear_menu()
        counter = itertools.count(start=1)
        [print(
            '{0}: {1} {2}'.format(
                str(next(counter)),
                movie["original_title"],
                movie['release_year']
            ))
            for movie in self.movie_list]
        print('{}: Find a different movie'.format(str(next(counter))))
        index = input('Choose which movie you want to watch \n> ')
        if int(index) - 1 == len(self.movie_list):
            self.get_movie_list()
        else:
            self.find_streaming_urls(index = int(index) - 1)

    def find_streaming_urls(self, index):
        clear_menu()
        guide_id = self.movie_list[index]["id"]
        result = self.search.movie_lookup_by_id(guide_id)
        if result['subscription_web_sources']:
            print(result['original_title'])
            [print('{0}: {1}'
                .format(url['display_name'], url['link']))
                for url in result['subscription_web_sources']
            ]
            pause()
        else:
            print('No subscription sources for this movie')
            pause()


if __name__ == '__main__':
    Menu().menu()
