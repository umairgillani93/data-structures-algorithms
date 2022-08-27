def sol(arr: str) -> int: 
  '''
  Returns the longest contiguous
  sum
  '''
  curr_sum = 0 
  max_sum = 0 

  print('\nArray is: {}'.format(arr))

  for i in range(len(arr)):
    curr_sum += arr[i]
    print('\nCurren sum at index: %s is %s' %(i, curr_sum))

    if curr_sum > max_sum:
      max_sum = curr_sum

    if curr_sum < 0:
      curr_sum = 0

  print('Max sum: {}'.format(max_sum))

if __name__ == '__main__':
  sol([-2, 3, -1, 2])



