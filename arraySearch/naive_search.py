# https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/?ref=lbp

def searchElem(arr, x):
    for i in len(arr):
        if arr[i] == x:
            return i


if __name__ == "main":
    arr = [1, 4, 5, 6, 9]
    print(searchElem(arr, 5))
