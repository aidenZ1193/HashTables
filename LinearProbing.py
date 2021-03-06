#!/usr/local/bin/python3
"""
Created on Mon May 20 2019

@author: Xiao Zhang
@id: 78369457
"""
from GenericHashClass import *

class LinearProbing(GenericHashClass):
    label = "Linear Probing"

    def __init__(self):
        GenericHashClass.__init__(self)
        self.N = 9887

    def set(self, key):
        index = self.hashFunction(key)
        # need to set in other cell
        if(self.hash_list[index] != None):
            index = self.linear_set(index)
            self.collisions += 1
        # check if the hash table is full
        if(index != -1):
            self.hash_list[index] = key
            self.num_elements += 1
        else:
            #print("The hash table is full.")
            pass

    # @return next available index
    def linear_set(self, index):
        full = False
        while(self.hash_list[index] != None):
            index += 1
            if(index == self.N):
                # if exceed N the second time
                if(full is True):
                    index = -1
                    break
                full = True
                index -= self.N

        return index
    
    def search(self, key):
        index = self.hashFunction(key)
        if(self.hash_list[index] == key):
            return True, index
        else:
            # have to search for the right one, continue with index
            rotate = False
            while(self.hash_list[index] != None and self.hash_list[index] != key):
                #index += 1
                index = (index+1)%self.N
                if(index == self.N):
                    # if exceed N the second time
                    if(rotate is True):
                        index = -1
                        break
                    rotate = True
                    index -= self.N
            if(index != -1 and self.hash_list[index] == key):
                return True, index
            else:
                #print("Didn't find the key.")
                return False, key

    def delete(self, key):
        flag, index = self.search(key)
        if flag == False:
            return False
        
        while(self.hash_list[index] is not None and self.hash_list[index] != key):
            index = (index+1)%self.N
        
        #if self.hash_list[index] is None:
        #    return False

        j = (index+1)%self.N
        while(self.hash_list[j] is not None):
            #print("Delete: i and j is: ", index, " ", j, " with key = ", key)
            origin_key = self.hash_list[j]%self.N
            #if(origin_key == self.hash_list)
            if(index < j and origin_key > index and origin_key <= j):
                pass
            elif j <= index and (origin_key > index or origin_key <= j):
                pass
            else:
                self.hash_list[index] = self.hash_list[j]
                #print("Delete: i and j is: ", index, " ", j, " with key = ", key, " swapped")
                index = j
            j = (j + 1) % self.N
        self.num_elements -= 1
        return True
                    

