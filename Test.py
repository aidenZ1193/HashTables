#!/usr/local/bin/python3
"""
Created on Mon May 20 2019

@author: Xiao Zhang
@id: 78369457
"""

from GenericHashClass import *
from LinearProbing import *
from ChainedHashing import *
from CuckooHashing import *
from QuadraticHashing import *

import time
import random

# testing parameters
runs = [1000, 2500, 5000, 7500, 9000]
#runs = [1000]
random_value = []
N = 9887

# stores the running time of all tests. 4 hashes * 5 numbers * 3 tests
seq_results = []
colli_results = []
rand_results = []
# 4 * 3 insert tests, 12 number of collisions
# sequence: lp - chain - cuckoo - quadratic
collisions = []

# insert, search, and delete
# three operations for all four kinds of table
def tests(run, values, result, colli):
    hashes = []
    lp = LinearProbing()
    hashes.append(lp)
    ch = ChainedHashing()
    hashes.append(ch)
    qh = QuadraticHashing()
    hashes.append(qh)
    ck = CuckooHashing()
    hashes.append(ck)
    for n in range(4):
        if colli == 1 and hashes[n].label == "CuckooHashing":
            result.append(None)
            continue
        #print("Testing ", hashes[n].label)
        # Insertion
        start = time.time()
        for key in values:
            hashes[n].set(key)
        end = time.time()
        result.append((end-start)*1000)
        collisions.append(hashes[n].collisions)
        #print("Inserting ", run, " keys in ", (end-start)*1000, " ms with ", hashes[n].collisions, " collisions.")
        #print(hashes[n].hash_list)
        #print("Load factor is currently ", hashes[n].get_alpha())

        # Search
        flag = True
        correct = 0
        start = time.time()
        for key in values:
            flag, k = hashes[n].search(key)
            if flag == True:
                correct += 1
        end = time.time()
        result.append((end-start)*1000)
        #print("Searching ", run, " keys in ", (end-start)*1000, " ms with ", correct, " successes.")

        # Delect
        start = time.time()
        success = 0
        for key in values:
            flag = hashes[n].delete(key)
            if flag == True:
                success += 1
        end = time.time()
        result.append((end-start)*1000)
        #print("Deleting ", run, " keys in ", (end-start)*1000, " ms with ", success, " successes.")
        #print("Deleting ", run, " keys in ", (end-start)*1000, " ms.")
        print(hashes[n].label, " - ", format(result[-1], '0.2f'), " - ", format(result[-2], '0.2f'), " -", format(result[-3], '0.2f'), " - ", run, " - ", colli)

        #del hashes[n]
    del hashes


def random_data(run):
    value = []
    for x in range(run):
        rand = random.randint(0, N)
        while (rand in value):
            rand = random.randint(0, N)
        value.append(rand)
    return value

## generate random data and copy it 4 times.
def collision_data(run):
    value = random_data(run//4)
    value2 = [x*3 for x in value]
    value3 = [x*6 for x in value]
    value4 = [x*9 for x in value]
    value.extend(value2)
    value.extend(value3)
    value.extend(value4)
    return value

if __name__== "__main__":
    # sequencial, collision, and random data.
    results = []
    # three types of data
    print("Hash function - Insert - Search - Delete - Num - Type")

    for n in range(3):
        r = []
        results.append(r)
        # three numbers of data size
        for run in runs:
            if n == 0:
                #continue
                #print("Testing for seqiential data.")
                # sequential data
                values = [x for x in range(n, run)]
            if n == 1:
                #continue
                #print("Testing for heavily collision data.")
                # collision data
                values = collision_data(run)
            if n == 2:
                #continue
                #print("Testing for random data.")
                # random data
                values = random_data(run)
            #elif n == 1:
            #    values = 
            tests(run, values, results[n], n)
    
            #print("Hash function - Insert - Search - Delete - Num")
            #print()