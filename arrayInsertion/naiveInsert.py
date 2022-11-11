# https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/?ref=lbp

def insertElem(xs, x):
    xs.append(x)
    return xs


if __name__ == "main":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(insertElem(arr, 8))
