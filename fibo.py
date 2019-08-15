f1 = 1
f2 = 2
n = int(input())
if n ==1:
    print(f1)
elif n==2:
    print(f1)
    print(f2)
else:
    print(f1)
    print(f2)
    i = 3
    while(i <=n):
        f3 = f1 + f2
        print(f3)
        f1 = f2
        f2 = f3
        i = i+1
        pass
    pass
