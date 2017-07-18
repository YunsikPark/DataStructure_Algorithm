# import random
#
# source = [x for x in range(10)]
# random.shuffle(source)
#
# def bubblesort(x):
#     length = len(x)-1
#
#     for i in range(length):
#         for j in range(length -i):
#             if x[j] > x[j+1]:
#                 x[j], x[j+1] = x[j+1], x[j]
#                 # print(x)
#
#             # print(x)
#
#     return x
#
# bubblesort(source)
#
# print(source)

def bubble_sort(data):
    data_len = len(data)

    for i in range(data_len - 1):
        for j in range(data_len -i -1):
            if data[j] > data[j+1]:
                data[j], data[j+1]  = data[j+1], data[j]

if __name__ == "__main__":
    li = [2,3,5,2,3,8,6,7,10,8,1,4]
    bubble_sort(li)
    print(li)

