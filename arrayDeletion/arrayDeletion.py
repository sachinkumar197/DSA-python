# https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/?ref=lbp

def findElem(xs, d):
    for i in range(len(xs)):
        if xs[i] == d:
            return i
    return -1


def deleteElem(xs, d):
    _index = findElem(xs, d)
    for i in range(_index, len(xs)-1):
        xs[i] = xs[i + 1]
    return xs[:len(xs)-1]


if __name__ == "main":
    xs = list(range(7))
    print(deleteElem(xs, 4))
