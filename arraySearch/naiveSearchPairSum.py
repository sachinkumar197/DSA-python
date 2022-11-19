# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=lbp

def searchElem(xs, val):
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            if xs[i] + xs[j] == val:
                return "Yes"
    return "No"


A = [0, -1, 2, -3, 1]
x = -2
print(searchElem(A, x))
