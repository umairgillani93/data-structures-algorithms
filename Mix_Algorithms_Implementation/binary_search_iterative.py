def binary_search_iterative(arr, x):
    """sorts the array by dividing array into two halves
    iteratively"""

    if len(arr) > 1:
        mid = len(arr) // 2
        
        first_half = arr[: mid]
        second_half = arr[mid :]
        
        if x == arr[mid]:
            return True
        
        elif x < arr[mid]:
            i = 0
            while i <= len(first_half):
                if first_half[i] == x:
                    return True
                else:
                    i += 1
                    
        elif x > arr[mid]:
            j = 0 
            while j < len(second_half):
                if second_half[j] == x:
                    return True
                else:
                    j += 1
                    
        else:
            return f"X: {x} no in array!"
        
    else:
        return -1

A = [1,2,3,4,8,9]
item = 9
