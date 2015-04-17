import random

A = list(map(int, raw_input().split()))
#median, or if even number of items in left, 
#the item to the left of the median
k = len(A)/2 
def quick_select(A, k):
    pivot = random.choice(A)

    A1 = []
    A2 = []

    for i in A:
        if i < pivot:
            A1.append(i)
        else:
            A2.append(i)

    if k < len(A1):
        return quick_select(A1, k)
    elif k > len(A) - len(A2):
        return quick_select(A2, k - (len(A) - len(A2)))
    else:
        return pivot

print quick_select (A, k)