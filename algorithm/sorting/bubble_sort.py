def bubbleSort(x):
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


import random

source = [x for x in range(10)]
random.shuffle(source)

def bubblesort(x):
    length = len(x)-1

    for i in range(length):
        for j in range(length -i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                # print(x)

            # print(x)

    return x

bubblesort(source)

print(source)