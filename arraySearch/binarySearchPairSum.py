# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=lbp

def binarySearch(i, j, ls, key):
    mid = (i + j) // 2
    if ls[mid] == key:
        return mid
    elif (j <= i + 1) | (i >= j):
        return -1
    elif key < ls[mid]:
        return binarySearch(i, mid, ls, key)
    elif key > ls[mid]:
        return binarySearch(mid + 1, j, ls, key)


def searchElem(xs, val):
    xs.sort()
    for i in range(len(xs) - 1):
        searchKey = val - xs[i]
        j = binarySearch(i + 1, len(xs) - 1, xs, searchKey)
        if j != -1:
            return "Yes"
    return "No"


A = [0, -1, 2, -3, 1]
x = -2
print(searchElem(A, x))
