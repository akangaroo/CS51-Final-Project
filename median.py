import random
import time

# test list
lst = [0,1,2,3,4,5,6,7,8,9,10,11]

def test(A, k):
    return sorted(A)[k]

# median, or if even number of items in left, 
# the item to the left of the median
def quick_select(A, k):
    lesser = []
    greater = []
    pivot = random.choice(A)
    indicator = True
    for i in A:
        if i < pivot:
            lesser.append(i)
        else:
            if i == pivot and indicator:
                indicator = False
            else:
                greater.append(i)
    if k <= len(lesser):
        return quick_select(lesser, k)
    elif k > len(A) - len(greater):
        return quick_select(greater, k - (len(A) - len(greater)))
    else:
        return pivot

def median_test(C):
   print counting_sort_med(C, 12)

# helper median (manual) for short lists
def short_median(A):
    return sorted(A)[len(A)/2]

# median of fives method
def median_of_fives(A):
    random.seed(time.time())
    random.shuffle(A)
    length = len(A)
    next = []
    if length <= 5:
        return short_median(A)
    else:
        for i in range(0, len(A)/5):
            next.append(short_median(A[5*i:5*i+5]))
        if len(A) > 5*len(A)/5:
            next.append(short_median(5*len(A)/5, len(A)))
        return median_of_fives(next)

#counting_
def counting_sort_med(A, m):
    hist = [0] * m
    for i in A:
        hist[i] = hist[i] + 1
    mid = len(A)/2
    for i in range(0, m):
        mid = mid - hist[i]
        if mid <= 0:
            return i

# called in main.py to compute median
def get_median(A):
    return quick_select(A, len(A)/2)

median_test(lst)