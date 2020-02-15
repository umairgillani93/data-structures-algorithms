# Recursion Problem01:

"""
Write a Recursive Fucntion which takes an integer and computes the comulative sum of "0"
to that integer.

For example, if n=4, the function should return 4+3+2+1+0, which equals 10
"""

def comulative_sum(n):
    # edge case0
    if n == 0:
        return 0

    # edge case1:
    elif n == 1:
        return 1

    else:
        return n + comulative_sum(n-1)

comulative = comulative_sum(4)
print(comulative)
