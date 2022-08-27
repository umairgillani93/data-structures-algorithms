def sol(arr: list) -> list:
  '''
  Returns reversed array
  time complexity: O(N)
  space complexity: O(N)
  '''

  return [
      arr[c] for c in range(len(arr) -1, -1, -1)
      ]

if __name__ == '__main__':
  print(sol([1,2,3,4,5]))
