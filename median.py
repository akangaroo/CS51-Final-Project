import random

lst = list(map(int, raw_input().split()))
#median, or if even number of items in left, 
#the item to the left of the median
def quick_select(A, k):
    lesser = []
    greater = []
    pivot = random.choice(A)
    for i in A:
        if i < pivot:
            lesser.append(i)
        else:
            greater.append(i)
    (a, a1, a2) = (len(A), len(lesser), len(greater))
    if k < a1:
        return quick_select(lesser, k)
    elif k > a - a2:
        return quick_select(greater, k - (a - a2))
    else:
        return pivot

def median_1 (C):
   print quick_select (C, len(C)/2)

median_1 (lst)