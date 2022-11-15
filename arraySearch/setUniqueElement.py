# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/?ref=lbp

def searchElem(xs):
    dedup_list = set(xs)
    temp = (sum(dedup_list) * 2) - sum(xs)
    return temp


x = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(searchElem(x))
