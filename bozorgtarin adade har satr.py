import numpy as np
def readArray(a):
    for i in range(0, 4):
        print("Enter row(", i + 1, "):")
        s = input().split (' ')
        for j in range(0, 4):
            a[i, j] = int(s[j])
def findmaxrow(a):
    for i in range(0, 4):
        a[i, 4] = a[i, 0]
        for j in range(1, 4):
            if a[i, 4] < a[i, j]:
                a[i, 4] = a[i, j]
def writearray(a):
    for i in range(0, 4):
        print ()
        for j in range(0,4):
            print (" ", a[i, j], end ='')
        print(" ", a[i, 4])
def main():
    a = np.zeros ((4, 5))
    readArray(a)
    findmaxrow(a)
    print("*********************result*****************")
    writearray(a)
main()
