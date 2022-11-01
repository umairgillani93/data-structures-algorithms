import os
import json

def sort_arr(arr):
    while True:
        corrected = False
        for k in range(len(arr) - 1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
            
                corrected = True

        if not corrected:
            return arr
        
assert sort_arr([7, 11, 3, 4, 1]) == [1,3,4,7,11]
print(sort_arr([7,11,3,4,1]))       
           

def linear_search(arr, k):
    '''
    searches the given item in array
    linearly, if item is there it comes up with index
    else returns -1
    
    '''
    i = 0
    while i < len(arr):
        if arr[i] == k:
            return i
        else:
            i += 1

    return -1

def bin_search_rec(arr, k):
    # edge  case
    arr = sort_arr(arr)
    if len(arr) == 1:
        return -1
    
    else:
        arr = sort_arr(arr)
        print(f'array: {arr}')

        # find the mid-point of array
        mid = len(arr) // 2
        
        # define left half
        left = arr[: mid]

        # define right half
        right = arr[mid :]

        if k == arr[mid]:
            return True
        elif k < arr[mid]:
            return bin_search_rec(left, k)

        else:
            return bin_search_rec(right, k)

def bin_search_iter(arr, k):
    '''
    finds the required element in array
    using iterative approach on two halves in each
    iteration
    '''
    if len(arr) > 1:
        # sort the array first
        arr = sort_arr(arr)
        print(f'arr: {arr}')

        # find the mid point
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        print(f'left: {left}')
        print(f'right: {right}')


        if k == arr[mid]:
            return True
        
        elif k < arr[mid]:
            i = 0
            while i < len(left):
                if left[i] == k:
                    return True
                else:
                    i += 1

        else:
            j = 0
            while j < len(right):
                if right[j] == k:
                    return True
                else:
                    j += 1

    else:
        return -1

def merge_sort(arr):
    '''
    sorts the array by divide-and-conquer method
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[: mid]
        right = arr[mid :]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                new_arr[k] = right[j]
                j += 1

            k += 1  


        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        return arr

    else:
        return arr


def quick_sort(arr):
    '''
    sorts an array using divide and conquer apporach
    '''
    # Array has to be sorted first
    arr = sort_arr(arr)
    # find the pivot item
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [y for y in arr if y == pivot]
    right = [z for z in arr if z > pivot]

    return quick_sort(left) + mid + quick_sort(right)

if __name__ == '__main__':
    print(quick_sort([2,4,7,2,1,3]))

