# https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/

def rotateByOne(x):
    i = 0
    j = len(x) - 1
    while i != j:
        x[i], x[j] = x[j], x[i]
        i += 1
    return x

test_array = list(range(13))
rotateByOne(test_array)
