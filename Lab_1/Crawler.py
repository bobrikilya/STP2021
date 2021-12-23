#from random import randint
from os import listdir
import random

class Crawler:

    def __init__(self, dir, verse_size_1, verse_size_2):
        self.dir = dir
        self.verse_size_1 = verse_size_1
        self.verse_size_2 = verse_size_2
        self.rows_list = []
        self.songs_list = listdir(self.dir)

    def crawl_function(self):
        for song in self.songs_list:
            with open(f'D\Projects Python\STP2021\Lab_1\\{self.dir}\\{song}', 'r', encoding='utf-8') as file:
                for row in file:
                    print(random.choice(file.readlines()))


Crawler()




