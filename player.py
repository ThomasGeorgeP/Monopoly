import pygame

class User():
    def __init__(self,name,icon):
        self.display_name=name
        self.picture=icon
        self.pic_rect=icon.get_rect()
    