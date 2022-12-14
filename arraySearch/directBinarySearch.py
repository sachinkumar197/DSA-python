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


# xs = [1, 2, 3, 4, 5, 0]
xs = list(range(15))
print(searchElem(0, len(xs), xs, 4))
