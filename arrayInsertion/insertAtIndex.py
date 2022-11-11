def insertElem(xs, n, d):
    xs.insert(n, d)
    return xs


if __name__ == "main":
    arr = list(range(7))
    print(insertElem(arr, 3, 40))
