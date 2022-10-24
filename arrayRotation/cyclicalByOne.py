# https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/

def rotate(x):
    temp = x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1]
    x[len(x) - 1] = temp
    return x


test_array = list(range(13))
rotate(test_array)
