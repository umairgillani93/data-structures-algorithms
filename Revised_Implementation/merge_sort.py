from typing import List

def merge_sort(arr: List[int]) -> List[int]:
  '''
  returns sorted array, by dividing and conquring method

  Time complexity: O(n*logn)
  '''
  if len(arr) > 1:
    mid = len(arr) // 2
    print('\nMid: {}'.format(mid))

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # Delare pointers
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


if __name__ == '__main__':
  print(merge_sort([11,7,4,1,2,9]))
