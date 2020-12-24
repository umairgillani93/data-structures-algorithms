def _min(arr):
    min_num = arr[0]
    
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            
    return min_num
    
print(_min([1,23,4]))
