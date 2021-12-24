from os import listdir
import random

class Crawler:

    def __init__(self, dir):
        self.dir = dir
        self.songs_list = listdir(self.dir)
        self.rows_set = set()

    def crawl_function(self):
        for song in self.songs_list:
            with open(self.dir + '\\' + song, 'r', encoding='utf-8') as file:
                for row in file:
                    self.rows_set.add(row)
        return self.rows_set

# cr = Crawler('songs', 3, 4)
# cr.crawl_function()




