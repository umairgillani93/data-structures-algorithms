# QuickSort implementation by UmairGillani -> Umairgillani93@gmail.com

from typing import List

def quick_sort(arr: List[int]) -> List[int]:
  '''
 returns sorted array implementing quick sort algorithm

 Time complexity: O(n * logn)
  '''

  # define base case
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]

  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
  print(quick_sort([2,4,7,2,1,4,3]))
  
