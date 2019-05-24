#!/usr/local/bin/python3
"""
Created on Mon May 20 2019

@author: Xiao Zhang
@id: 78369457
"""
from GenericHashClass import *

class ChainedHashing(GenericHashClass):
    label = "Chained Hashing"

    def __init(self):
        GenericHashClass.__init__(self)
        
    def set(self, key):
        index = self.hashFunction(key)
        if(self.hash_list[index] == None):
            self.hash_list[index] = []
        else:
            self.collisions += 1
        self.hash_list[index].append(key)
        self.num_elements += 1
    
    def search(self, key):
        index = self.hashFunction(key)
        if(self.hash_list[index] == None):
            return False, key
        for k in self.hash_list[index]:
            if key == k:
                return True, index
        return False, key
    
    def delete(self, key):
        flag, index = self.search(key)
        if flag == False:
            return False
        
        for k in self.hash_list[index]:
            if key == k:
                self.hash_list[index].remove(k)
        self.num_elements -= 1
        return True

