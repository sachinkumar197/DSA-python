def split_array(i, j, ls, key):
    mid = (i + j) // 2
    print("i,j,mid", i, j, mid, ls[mid])
    if ls[mid] == key:
        return mid
    elif j == i+1:
        return "not found"
    elif key < ls[mid]:
        return split_array(i, mid, ls, key)
    elif key > ls[mid]:
        return split_array(mid + 1, j, ls, key)


# xs = [1, 2, 3, 4, 5, 0]
xs = list(range(15))
print(split_array(0, len(xs), xs, 4))
