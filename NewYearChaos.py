#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    too_chaotic = False
    total_people = len(q)
    queue = [p for p in range(1, total_people + 1)]
    totalBribes = 0
    for i, e in reversed(list(enumerate(q))):
        briber = queue[i]
        briber_current_index = q.index(briber, 0, i + 1)
        briber_expected_index = i

        bribed = e
        bribed_current_index = i
        bribed_expected_index = queue.index(bribed, 0 , i + 1)

        # number of spots the briber has advanced
        bribes = briber_expected_index - briber_current_index
        if bribes > 2:
            too_chaotic = True
            break

        # number of times the bribed has been bribed. Not all bribes were from the current briber
        timesBribedBribed = bribed_current_index - bribed_expected_index
        totalBribes += timesBribedBribed

        queue.pop(bribed_expected_index)
        queue.insert(briber_expected_index, bribed)

        if(queue == q):
            break
    
    print(totalBribes if not too_chaotic else 'Too chaotic')
  
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
