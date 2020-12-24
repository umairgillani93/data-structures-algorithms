def merge_sort(arr):
    """sorts the given array in ascending order
    using divide and conquer principle recursively"""
    
    # base case check
    if len(arr) > 1:
        
        mid = len(arr) // 2
        first_half = arr[:mid]
        second_half = arr[mid:]
        
        merge_sort(first_half) # perform merge sort on first half 
        merge_sort(second_half) # perform merge sort on second half 
        
        i = j = k = 0 # index pointer for first, second and last list to be returned
        
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
                
            else:
                arr[k] = second_half[j]
                j += 1
                
            k += 1
            
        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1
            
        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1
            
        return arr 
    
    else:
        return arr

        
A = [1,11,3,5,5,2,19]
merge_sort(A)
