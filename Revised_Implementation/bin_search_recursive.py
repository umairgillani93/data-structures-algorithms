def bin_search_recursive(arr, k):
  '''
  checks if 'k' is present in given 'arr'
  using divide and conquer binary search approach
  retuns True if 'k' is in 'arr'
  else returns -1

  the only condition we have to keep in mind for binary search is
  the array has to be sorted in ascending order 

  Time complexity: O(logn)
  
  first iteration array length = n
  second iteration array length = n / 2
  third iteration array length = (n / 2) / 2 = n / 4

  In general n / 2^k

  Applying log on both sides 

  log(n),2 = log(2^k), 2
  
  k = log(n)

  '''

  # sort the array first 
  arr = sorted(arr)
  
  # check the length of arr if greater than 1
  if len(arr) > 1:
    # find mid value
    mid = len(arr) // 2

    left = arr[: mid]
    right = arr[mid :]

    # check if 'k' is middle item
    if k == arr[mid]:
      return True

    elif k < arr[mid]:
      return bin_search_recursive(left, k)

    else:
      return bin_search_recursive(right, k)
    

  else:
    return False

if __name__ == '__main__':
  print(bin_search_recursive([1], 1))


