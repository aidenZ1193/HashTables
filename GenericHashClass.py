# -*- coding: utf-8 -*-
"""
Created on Mon May 20 2019

@author: Xiao Zhang
@id: 78369457
"""
import random
import time

class GenericHashClass(object):
    
    def __init__(self):
        self.collisions = 0
        self.N= 9887
        self.hash_list = [None] * self.N
        self.num_elements = 0
        self.alpha = 0.0

    def hashFunction(self, key):
        index = key % self.N
        return index
    
    def get_alpha(self):
        self.alpha = self.num_elements//self.N
        return self.alpha

    

