def _max(arr):
    max_num = arr[0]
    
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            
    return max_num

print(_max([1,23,4]))
