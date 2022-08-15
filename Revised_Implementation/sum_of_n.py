import time 
from typing import List 

def sum_of_n_numbers(n: int) -> int:
  '''
  returns sum of 'n' numbers by implementing
  mathematical formula
  '''
  return n * (n + 1) / 2

def _sum_of_n_numbers2(n: int) -> int:
  sum_ = 0
  for i in range(n):
    sum_ += i

  return sum_


start
