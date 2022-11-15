# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/?ref=lbp

def searchElem(xs):
    temp_dict = {}
    for i in range(len(xs)):
        if xs[i] in temp_dict.keys():
            return xs[i]
        else:
            temp_dict[xs[i]] = 1
    return -1


arr = [9, 8, 2, 6, 1, 8, 5, 3]
print(searchElem(arr))
