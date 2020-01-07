# Find the larges continuous sum of given Array
def large_cont_sum(arr):

    # Edge case
    if len(arr) == 0:
        return 0

    # start max current sum at first index
    max_sum = current_sum = arr[0]

    # for every element in the array do the following 
    for num in arr[1:]:
        # set current sum as the higher of two 
        current_sum = max(current_sum+num, num)

        # set maximum as the higher between the currentSum and the current_max 
        max_sum = max(current_sum, max_sum)


    return max_sum 

print(large_cont_sum([-1,-5,0,1,7,10,10,-10]))