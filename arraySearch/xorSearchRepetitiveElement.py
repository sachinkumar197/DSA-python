# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/?ref=lbp

def searchElem(xs):
    xor1 = 1
    for i in range(2, len(xs)):
        xor1 ^= i
    xor2 = xs[0]
    for i in range(1, len(xs)):
        xor2 ^= xs[i]
    return xor1 ^ xor2


arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
print(searchElem(arr))
