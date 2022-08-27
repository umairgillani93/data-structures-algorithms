def sol(arr: list, k: int) -> list:
 '''
 returns pair sums
 '''
 pairs = []

 i = 0 
 j = len(arr) - 1

 while i < j:
   if arr[i] + arr[j] == k:
     pairs.append((arr[i], arr[j]))
   else:
     i += 1
     j -= 1

 return pairs 

if __name__ == '__main__':
  print(sol([1,5,7,1], 6))



