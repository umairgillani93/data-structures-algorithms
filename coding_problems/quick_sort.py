def quick_sort(arr: list) -> list:
  '''
  Returns array using quick-sort algorithm
  '''
  if len(arr) > 1:
    pivot = arr[len(arr) // 2]
    print(f'privot: {pivot}')

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 

    return quick_sort(left) + middle + quick_sort(right)
  
  else:
    return arr

if __name__ == '__main__':
  print(quick_sort([11,29,2,7,10]))


