#!/usr/local/bin/python3
"""
Created on Mon May 20 2019

@author: Xiao Zhang
@id: 78369457
"""
from GenericHashClass import *

## Need two hashing function:
## 1: key%N
## 2: key*2%N
class CuckooHashing(GenericHashClass):
    label = "CuckooHashing"

    def __init__(self):
        GenericHashClass.__init__(self)
        self.N = 5501 #9887
        self.table1 = [None]*self.N
        self.table2 = [None]*self.N
        self.key_list = []
        
    def hash1(self, key):
        return key%self.N
    
    def hash2(self, key):
        #return key*self.hash_2_factor%self.N
        return int((key/self.N) % self.N)

    # return the stored key in spot
    def hashFunction(self, t, key):
        if t == 0:
            i = self.hash1(key)
            #print("1, key is", key,"index is ", i)
            value = self.table1[i]
            self.table1[i] = key
        else:
            i = self.hash2(key)
            #print("2, key is", key,"index is ", i)
            value = self.table2[i]
            self.table2[i] = key
        return value
    
    def isPrime(self, n):
        if n==2 or n==3: return True
        if n%2==0 or n<2: return False
        for i in range(3,int(n**0.5)+1,2):  
            if n%i==0:
                return False    

        return True

    ## clear both tables and rehash all of the keys
    def rehash(self):
        #self.hash_2_factor += 1
        self.N += 2
        while(self.isPrime(self.N) == False):
            self.N += 2
        del self.table1
        del self.table2
        self.table1 = [None]*self.N
        self.table2 = [None]*self.N
        l = self.key_list
        self.key_list = []
        for k in l:
            self.set(k)
    
    ## idea: 
    def set(self, key):
        t = 0
        iteration = 0
        ## store all keys in the list, and rehash all of them
        self.key_list.append(key)
        while(key != None):
            key = self.hashFunction(t, key)
            t = 1-t
            if iteration > 0:
                self.collisions += 1
            iteration += 1
            if(iteration >= 10):
                self.rehash()
                iteration = 0
        #print("table 1:", self.table1)
        #print("table 2:", self.table2)

    def search(self, key):
        i = self.hash1(key)
        if(self.table1[i] == key):
            return 1, i
        else:
            i = self.hash2(key)
            if(self.table2[i] == key):
                return 2, i
            else:
                return -1, key
    
    def delete(self, key):
        flag, i = self.search(key)
        if flag > 0:
            if flag == 1:
                self.table1[i] = None
            else:
                self.table2[i] = None
            return True
        else:
            return False
    

'''
if __name__ == "__main__":
    keys = [1,3,5,7,9,11,13,14,19,33, 34, 35,36, 2, 4]
    ch = CuckooHashing()
    for k in keys:
        ch.set(k)
    co = 0
    for k in keys:
        flag, i = ch.search(k)
        if flag > 0:
            co += 1
            if flag == 1:
                print("in table 1 with index = ", i, " key is ", k, " ", ch.table1[i])
            else:
                print("in table 2 with index = ", i, " key is ", k, " ", ch.table2[i])
    print("currect search: ", co)
    '''