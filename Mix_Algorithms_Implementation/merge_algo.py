def Merge(arr1, arr2):
    arr3 = [None] * len(arr1)
    
    # REMEMBER: arr1 and arr2 have to be sorted
    i = j = k = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
            
        else:
            arr3[k] = arr2[j]
            j += 1
            
        k += 1
        
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
    
    return arr
