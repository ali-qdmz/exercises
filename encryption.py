s = input('insert string')


def encryptor(e):
    res = ""
    for i in e:
        x = ord(i)
        x = x+1
        x2 = chr(x)
        res = res + x2
    return res

def decryptor(e):
    res = ""
    for i in e:
        x = ord(i)
        x = x-1
        x2 = chr(x)
        res = res + x2
    return res

print(encryptor(s))
print(decryptor(encryptor(s)))

