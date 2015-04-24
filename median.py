import random

lst = [1,2,3,4,5,6,7,8,9,10]

def test(A, k):
    return sorted(A)[k]

#median, or if even number of items in left, 
#the item to the left of the median
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
    (a, a1, a2) = (len(A), len(lesser), len(greater))
    if k <= a1:
        return quick_select(lesser, k)
    elif k > a - a2:
        return quick_select(greater, k - (a - a2))
    else:
        return pivot

def median_1(C):
   print quick_select (C, len(C)/2)

median_1(lst)

#helper median (manual) for short lists
def short_median(A):
    return sorted(A)[len(A)/2]

#median of fives method
def median_of_fives(A):
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

print median_of_fives(lst)

