arr = [1,2,3,4,5]
new_arr = []
new_arr.append(arr[len(arr) -1])
 
for x in arr[:-1]:
  new_arr.append(x)

print(f'new_arr: {new_arr}')

assert len(arr) == len(new_arr)
