# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/?ref=lbp

def searchElem(xs):
    xs.sort()
    for i in range(len(xs)):
        if xs[i] != i + 1:
            return xs[i]
    return -1


arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
print(searchElem(arr))
