def sol(arr: list) -> int:
  '''
  returns rotated list in clock-wise direction 
  by one unit
  '''
  new_arr = []

  new_arr.append(arr[-1])

  for x in arr[:-1]:
    print(x)
    new_arr.append(x)

  return new_arr

if __name__ == '__main__':
  print(sol([1,2,3,4,5]))
  

      

