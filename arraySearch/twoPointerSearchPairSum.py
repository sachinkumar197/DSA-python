# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=lbp

def searchElem(xs, left, right, val):
    xs.sort()
    if left >= right:
        return "No"
    elif xs[left] + xs[right] == val:
        return "Yes"
    elif xs[left] + xs[right] > val:
        return searchElem(xs, left, right - 1, val)
    elif xs[left] + xs[right] < val:
        return searchElem(xs, left + 1, right, val)
    return "No"


A = [0, -1, 2, -3, 1]
x = -2
print(searchElem(A, 0, len(A)-1, x))
