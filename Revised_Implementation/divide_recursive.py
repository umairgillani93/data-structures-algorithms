from typing import List

def divide_recursive(arr: List[int]) -> List[int]:
  ''' 
  divides the given array into 'n' multiple arrays
  till that each array is left with only one item
  '''

  cnt = 1
  if len(arr) > 1:
    mid = len(arr) // 2

    left = arr[: mid]
    right = arr[mid :]

    print('\nNo. of iteration: {}'.format(cnt))
    print('\nMid value: {}'.format(mid))
    print('\nLeft side array: {}'.format(left))
    print('\nRight side array: {}'.format(right))

    divide_recursive(left)
    divide_recursive(right)
    
    cnt += 1


  else:
    print('Array lengths are equal to 1')


if __name__ == '__main__':
  print(divide_recursive([1,2,3,4,5,6,7,8,10]))

