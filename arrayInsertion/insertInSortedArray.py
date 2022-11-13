# https://www.geeksforgeeks.org/search-insert-and-delete-in-a-sorted-array/?ref=lbp

def insertElem(xs, key):
    xs.append(0)
    for i in range(len(xs)):
        if key <= xs[i]:
            for j in range(len(xs) - 1, i, -1):
                xs[j] = xs[j-1]
            xs[i] = key
            return xs
    xs[len(xs)-1] = key
    return xs


x = list(range(12))
print(insertElem(x, -100))
