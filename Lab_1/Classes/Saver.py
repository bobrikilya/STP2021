class Saver:

    def __init__(self):
        pass

    def saver_function(self, lyrics_list):
        with open('..\lovely_song.txt', 'w', encoding='utf-8') as file:
            file.write(lyrics_list[2] + '\n\n' + lyrics_list[0] + '\n\
            \n' + lyrics_list[2] + '\n\n' + lyrics_list[1] + '\n\n' + lyrics_list[2])

# Saver().saver_function(['1', '2', '3'])