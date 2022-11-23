# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=lbp

def searchElem(xs, val):
    rem_array = [0] * val
    for i in range(len(xs)):
        if xs[i] < val:
            rem_array[xs[i]] += 1
    print(rem_array)

    for i in range(1, val // 2):
        if rem_array[i] > 0 and rem_array[val - i] > 0:
            return "Yes"
    return "No"


A = [1, 4, 45, 6, 10, 8]
x = 16
print(searchElem(A, x))
