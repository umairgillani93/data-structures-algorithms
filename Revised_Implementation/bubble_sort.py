# Bubble sort implementation by UmairGillani -> umairgillani93@gmail.com

from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
  '''
  returns the sorted array using bubble sort algorithm

  Time complexity: O(n^2)
  '''

  # Start infinite loop
  while True:
    # Set flag vaiable
    corrected = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i+1]:
        arr[i+1], arr[i] = arr[i], arr[i+1]
        corrected = True

    if not corrected:
      return arr

if __name__ == '__main__':
  print(bubble_sort([4,2,1,3]))
