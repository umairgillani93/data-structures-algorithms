def linear_search(arr, x):
    """searches the given array linearly, and returns True
    if given item in present in array"""
    
    idx = 0  # starting index 
    while idx < len(arr):  
        if arr[idx] == x:
            return True, idx 
        else:
            idx += 1
            
linear_search([1,2,3,4,5], 5)
