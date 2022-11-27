# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/?ref=lbp

def searchElem(xs, val):
    temp_hash = {}
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            temp_val = val - xs[i] - xs[j]
            if temp_val in temp_hash.keys():
                print(xs[i], xs[j], temp_val)
                return True
            elif xs[j] not in temp_hash.keys():
                temp_hash[xs[j]] = 1
    return False


A = [1, 4, 45, 6, 10, 8]
sum = 22
searchElem(A, sum)
