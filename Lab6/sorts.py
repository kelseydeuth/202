#
#Kelsey Deuth
#kdeuth@calpoly.edu
#05/15/19
#
#Lab6
#Section 11
#This code preforms an insertion sort and selection sort
#

import random
import time


def selection_sort(list):
    c = 0
    for num in range(len(list)):
        m = num
        for i in range(num + 1, len(list)):
            c += 1
            if list[m] > list[i]:
                m = i
        list[num], list[m] = list[m], list[num]  # Swap the found minimum element
    return c


def insertion_sort(list):
    if len(list) == 0:
        return 0
    c = 0
    for num in range(1, len(list)):
        k = list[num]
        j = i - 1
        while True:
            if j >= 0:
                c += 1
                if k < list[j]:
                    list[j + 1] = list[j]
                    j -= 1
                else:
                    break
            else:
                break
        list[j + 1] = k
    return c
   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()


