#!/usr/bin/python3
'''moudle for base class'''
Class Base:
   '''A repreasention of the base of opp'''
    __nb_objects = 0
    
    def __init__(self, id=None):
       '''costructor'''
        if id is not None:
           self.id = id
        else:
            base.__nb_objects += 1
            self.id = __nb_objects
