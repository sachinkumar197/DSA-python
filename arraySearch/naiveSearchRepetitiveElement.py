# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/?ref=lbp

def searchElement(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return xs[i]
    return -1


x = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
print(searchElement(x))
