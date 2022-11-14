# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/?ref=lbp

def searchElem(xs):
    i = 0
    while i < len(xs):
        count = 0
        j = 0
        while j < len(xs):
            if (i != j) & (xs[i] == xs[j]):
                count += 1
                break
            j += 1
        if count == 0:
            return xs[i]
        i += 1
    return -1


x = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(searchElem(x))
