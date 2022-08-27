def _index(arr: list, item: int) -> int:
  '''
  Returns the item of index in an array
  '''
  for idx, val in enumerate(arr):
    if val == item:
      return idx

assert _index([1,2,34], 34) == 2
def sol(arr: list, k: int):

  for i in range(len(arr)):
    sum_  = sum(arr[i:])
    if sum_ == k:
      new_arr = arr[i:]

      #return (arr.index(new_arr[0]), arr.index(new_arr[-1]))
      return _index(arr, new_arr[0]), _index(arr, new_arr[-1])
    else:
      continue 


if __name__ == '__main__':
  print(sol([1,2,3,7,5], 12))

