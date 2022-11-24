# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/?ref=lbp

def twoPointerSearch(xs, left, right, val):
    xs.sort()
    if left >= right:
        return False
    elif xs[left] + xs[right] == val:
        print(xs[left], xs[right], end=" ")
        return True
    elif xs[left] + xs[right] > val:
        return twoPointerSearch(xs, left, right - 1, val)
    elif xs[left] + xs[right] < val:
        return twoPointerSearch(xs, left + 1, right, val)
    return False


def searchElem(xs, val):
    xs.sort()
    for i in range(len(xs) - 2):
        result = twoPointerSearch(xs, i + 1, len(xs) - 1, val - xs[i])
        if result:
            print(xs[i], end="\n")
            return True
    return False


A = [1, 4, 45, 6, 10, 8]
_sum = 22
searchElem(A, _sum)
