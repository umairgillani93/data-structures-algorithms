def sort(arr: list) -> list:
  '''
  Sorts the given arraay in ascending order
  '''
  while True:
    corrected = False
    for i in range(len(arr) -1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        corrected = True
      
    if not corrected:
      return arr

if __name__ == '__main__':
  print(sort([10,9,8,11,2,1]))

