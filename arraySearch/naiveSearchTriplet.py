# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/?ref=lbp

def searchElem(xs, val):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            for k in range(j + 1, len(xs)):
                if xs[i] + xs[j] + xs[k] == val:
                    print(xs[i], xs[j], xs[k])
                    return True
    return False


A = [1, 4, 45, 6, 10, 8]
_sum = 22
searchElem(A, _sum)
