# https://www.geeksforgeeks.org/search-insert-and-delete-in-a-sorted-array/?ref=lbp

def searchElem(i, j, ls, key):
    mid = (i + j) // 2
    if ls[mid] == key:
        return mid
    elif (j <= i + 1) | (i >= j):
        return -1
    elif key < ls[mid]:
        return searchElem(i, mid, ls, key)
    elif key > ls[mid]:
        return searchElem(mid + 1, j, ls, key)


def deleteElem(xs, d):
    _index = searchElem(0, len(xs) - 1, xs, d)
    if _index != -1:
        for i in range(_index, len(xs) - 1):
            xs[i] = xs[i + 1]
        return xs[:len(xs) - 1]
    return xs


x = list(range(7))
print(deleteElem(x, 5))
