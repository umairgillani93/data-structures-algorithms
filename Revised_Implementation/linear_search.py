def linear_search(arr, k):
  '''
   takes an array and an item k
   checks if 'k' is present in array
   returns the index at which 'k' is present
   else returns -1
   
   Time compelxity: O(n)

  '''
  # declare a pointer
  i = 0

  while i < len(arr):
    if arr[i] == k:
      return i
    else:
      i += 1
  
  return -1

if __name__ == '__main__':
  print(linear_search([1,2,3,4,5], 6))
