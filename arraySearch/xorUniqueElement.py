# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/?ref=lbp

def searchElem(xs):
    init = xs[0]
    for i in range(1, len(xs)):
        init = init ^ xs[i]
    return init


x = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(searchElem(x))
