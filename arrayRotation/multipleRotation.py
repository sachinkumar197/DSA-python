# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

def reverse_array(x):
    for i in range(len(x) // 2):
        x[i], x[len(x) - i - 1] = x[len(x) - i - 1], x[i]
    return x


def rotateArray(x, d):
    d = d % len(x)
    x = reverse_array(x)
    left_array = reverse_array(x[:-d])
    right_array = reverse_array(x[-d:])
    return left_array + right_array


test_array = list(range(10))
print(rotateArray(test_array, 3))
