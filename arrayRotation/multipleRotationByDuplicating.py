# https://www.geeksforgeeks.org/quickly-find-multiple-left-rotations-of-an-array/

def rotate_array(x, k):
    i = k % len(x)
    j = i + len(x)
    x = x + x
    return x[i:j]


xs = list(range(7))
rotate_array(xs, 51)
