# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/?ref=lbp

def searchElem(xs):
    sum_of_first_n_elements = (len(xs) * (len(xs) - 1)) // 2
    temp = sum(xs) - sum_of_first_n_elements
    return temp


arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
print(searchElem(arr))
