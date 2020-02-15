n = 343
remainder = 0
for i in str(n):
    # while len()
    remainder = n%10
    quotient = n//10
    print("remainder: ",remainder)
    print("quotient: ",quotient)
    remainder += remainder
    if len(str(quotient)) == 1:
        break

print(remainder)
