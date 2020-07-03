#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    too_chaotic = False
    total_people = len(q)
    queue = [p for p in range(1, total_people + 1)]
    totalBribes = 0
    for i in range(total_people + 1):
        i = total_people - i - 1
        briber = queue[i]
        briber_expected_index = i
        # the briber can't be two places ahead of its original location
        briber_original_index = briber - 1
        if briber_original_index > 1:
            try:
                start = briber_original_index -2
                end = briber_original_index + 1
                q.index(briber, start, end)
            except ValueError:
                too_chaotic = True
                break

        bribed = q[i]
        bribed_current_index = i
        bribed_expected_index = queue.index(bribed, 0 , i + 1)              

        # number of times the bribed has been bribed. Not all bribes were from the current briber
        timesBribedBribed = bribed_current_index - bribed_expected_index
        totalBribes += timesBribedBribed

        queue.pop(bribed_expected_index)
        queue.insert(briber_expected_index, bribed)

        if(queue == q):
            break
    
    print(totalBribes if not too_chaotic else 'Too chaotic')
  
if __name__ == '__main__':

    f = open('NewYearChaos-Case9.txt', 'r')

    t = int(f.readline())

    for t_itr in range(t):
        n = int(f.readline())

        q = list(map(int, f.readline().rstrip().split()))

        minimumBribes(q)
