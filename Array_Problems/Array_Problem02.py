def pairSum(arr, k):

    # Edge case 
    if len(arr) < 2:
        return 
    
    else:
        tup_list = [(i,j) for i in arr for j in arr if i+j == k]
        tup_set = set(tup_list) 

    # return tup_set 
    print('\n'.join(map(str, tup_set)))

print(pairSum([1,3,2,2], 4))    