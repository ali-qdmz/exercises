from array import *
def prim (a, tedad, num):
    for i in range(0, tedad):
        if num % a[i] == 0:
            return 0
    a.append(0)
    a[tedad] = num
    return 1
def find_two_numbers (p, n1, n2, tedad, n):
    for i in range(0, tedad - 1):
        for j in range(i + 1, tedad):
            if (p[i] + p[j]) == n:
                n1 = p[i]
                n2 = p[j]
                return [n1, n2]
    return n1
def main():
    p = array ('i', [])
    i = 0
    j = 0
    tedad = 0
    n = 0
    done = 'Y'
    while True:
        tedad = 0
        n = int(input("Enter n:"))
        if n % 2 == 1:
            print("Enter a even number\n")
            continue
        for i in range(2, n+1):
            if prim(p, tedad, i) == 1:
                tedad= tedad + 1
        [i, j] = find_two_numbers(p, i, j, tedad - 1, n)
        print(n , " = ", i, " + ", j)
        done = input("You want to continue(y/n):")
        if done[0] == 'n' or done == 'N':
            return
main()
    
