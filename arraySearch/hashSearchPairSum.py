# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=lbp

def searchElem(xs, val):
    temp_dict = {}
    for i in range(len(xs)):
        searchKey = val - xs[i]
        if searchKey in temp_dict.keys():
            return "Yes"
        else:
            temp_dict[xs[i]] = 0
    return "No"


A = [0, -1, 2, -3, 1]
x = -2
print(searchElem(A, x))
