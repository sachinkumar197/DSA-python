# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/?ref=lbp

def searchElem(xs):
    _hash = {}
    for i in range(len(xs)):
        if xs[i] in _hash.keys():
            _hash[xs[i]] += 1
        else:
            _hash[xs[i]] = 1
    for key, value in _hash.items():
        if value == 1:
            return key


x = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(searchElem(x))
