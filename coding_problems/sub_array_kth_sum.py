def sol(arr: list, k: int) -> list:

  curr_sum = 0
  i_bounds = []
  
  upper = 0
  lower = 0

  for i in range(len(arr)):
    for j in range(len(arr)):

