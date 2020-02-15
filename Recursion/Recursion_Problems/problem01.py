# Recursion Problem02:
"""Given an integer, write a function which returns the sum of all the
individual digits in that integer.

For example: if n=4321, the function should return 4+3+2+1"""

other than recursion approach
def sum(n):
    n = str(n)
    str_list = []
    for i in range(len(n)):
        str_list.append(n[i])
    sum = 0
    for ele in str_list:
        sum += int(ele)

    return sum

s = sum(4321)
print(s)

# using recursion:
def rec_sum(n):
    if len(str(n)) == 1:
        return n

    else:
        return n%10 + rec_sum(n//10)


rs = rec_sum(4321)
print(rs)
