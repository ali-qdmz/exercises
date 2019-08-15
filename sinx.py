import math
def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
        pass
    return result

sign = 1
sum1 = 0
x = float(input('insert x value'))
n = int(input('insert n value'))
for i in range(1,n+1,2):
    sum1 = sign*(pow(x,i)/math.factorial(i)) + sum1
    sign = -1*sign
print(sum1)
