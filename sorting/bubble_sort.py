from random import randint

# create randomized array of length "length"
# array integer are of range 0, maxint


def create_array(length = 10, maxint = 50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


# apply bubble sort to the input array
def bubble_sort(arr):

    swapped = True

    while swapped:
        swapped = False

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

                swapped = True
    return arr


# return true is passed array is sorted
def is_sorted(arr):
    new_sorted_arr = sorted(arr)
    return arr == new_sorted_arr


def benchmark(n =[10, 100, 1000, 10000]):
    from time import time
    b0 = []  # bubble sort time
    b1 = []  # built-in sort time
    for length in n:
        unsorted_arr = create_array(length, length)

        t0 = time()
        builtinsort = sorted(unsorted_arr)  # sort with python built-in sort
        t1 = time()
        b1.append(t1-t0)  # record built-in time

        t0 = time()
        bubblesort = bubble_sort(unsorted_arr)  # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0)  # record bubble time
        # break
    print(b1)
    print(b0)
    print("n \t Built-In\t Bubble Sort")
    print("_______________________________________________")

    for i, cur_n in enumerate(n):
        # print(n, i , cur_n)
        print("%d\t%0.5f \t%0.5f"%(cur_n, b1[i], b0[i]))


benchmark()  # run benchmark function to analyze run time of bubble sort and python built-in sorted function

# new_arr = create_array()
#
# print("unsorted_array : : ", new_arr)
#
# sorted_arr = bubble_sort(new_arr)
#
# print("sorter_array : : ", sorted_arr)
#
# print(is_sorted(sorted_arr))


