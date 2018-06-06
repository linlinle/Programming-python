# -*- coding: utf-8 -*-
import webbrowser

class  Movie():
    '''This class provide a way to store Movie_Website related information'''
    VAILD_RATINGS = ['G','PG','PG-13','R']
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_storyline
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)