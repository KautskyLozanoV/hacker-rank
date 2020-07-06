#!/bin/python3

def findValueIndex(dict, value, start = 0, end = 0):
    if end == 0:
        end = len(dict)

    if start < 0:
        start = 0

    for i in range(start, end):
        currentValue = dict[i]
        if value == currentValue:
            return i

# Complete the minimumBribes function below.
def minimumBribes(q):
    too_chaotic = False
    total_people = len(q)
    queue = {p: p+1 for p in range(0, total_people)}
    total_bribes = 0
    for i in range(total_people):
        i = total_people - i - 1

        current = q[i]
        if current - (i+1) > 2:
            too_chaotic = True
            break

        original = queue[i]
        if current == original:
            continue
        elif current > original:
            # current is a briber
            if current - original > 2:
                too_chaotic = True
                break
        else:
            # current was bribed
            current_index_in_original = findValueIndex(queue, current, current - 3, i + 1)
            if current_index_in_original == None:
                too_chaotic = True
                break

            total_bribes += i - current_index_in_original            
            for j in range(current_index_in_original, i):                                
                queue[j], queue[j+1] = queue[j+1], queue[j]
       
    print(total_bribes if not too_chaotic else 'Too chaotic')
  
if __name__ == '__main__':

    f = open('NewYearChaos-Case9.txt', 'r')

    t = int(f.readline())

    for t_itr in range(t):
        n = int(f.readline())

        q = list(map(int, f.readline().rstrip().split()))

        minimumBribes(q)
