# https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/

def rotate_array(x, d):
    if len(x) > d:
        L = x[:d]
        R = x[d:]
        return split_array(L, R)
    else:
        print("no. of elements to be rotated are more than the length of the list ")


def split_array(L, R):
    if len(L) > len(R):
        Ll = L[:len(R)]
        Lr = L[len(R):]
        return R + split_array(Lr, Ll)
    elif len(L) < len(R):
        Rl = R[:-len(L)]
        Rr = R[-len(L):]
        return split_array(Rr, Rl) + L
    else:
        return R + L


test_array = list(range(15))
print(rotate_array(test_array, 3))
