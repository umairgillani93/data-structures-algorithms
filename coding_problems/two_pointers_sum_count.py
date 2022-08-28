def merge_sort(arr):
  '''
  sorts the array by recursively dividing and 
  than mergin all elements
  '''

  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid :]
  

    # keeps dividing recurseively untill 
    # the arrays are left with single elements
    merge_sort(left)
    merge_sort(right) 

    # declare pointers 
    i = 0
    j = 0 
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1

      else:
        arr[k] = right[j]
        j += 1

      k += 1

    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
      
  return arr

def sol(arr: list, k: int) -> list:
 '''
 returns pair sums
 '''
 pairs = []
 arr = sorted(arr)  

 i = 0 
 j = len(arr) - 1

 while i < j:
   if arr[i] + arr[j] == k:
     pairs.append((arr[i], arr[j]))
     i += 1
     j -= 1

   elif arr[i] + arr[j] > k:
     j -= 1

   else:
     i += 1

 return pairs


if __name__ == '__main__':
  print(sol([2, 3, 5, 8, 9, 10, 11], 17))

