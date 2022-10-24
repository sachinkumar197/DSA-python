def rotateByOne(xs):
    return xs[-1:] + xs[:-1]


test_array = list(range(13))
rotateByOne(test_array)
