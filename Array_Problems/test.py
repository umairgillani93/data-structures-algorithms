# finding pair sum 
def pairSum(arr, k):

    # Edge case 
    if len(arr) < 2:
        return # returns nothing 

    seen = set() 
    output = set() 

    for num in arr:

        target = k-num 

        if target not in seen:
            seen.add(num)
        
        else:
            output = ((min(num, target), max(num, target)))

    return len(output)

print(pairSum([1,3,2,2], 4))
