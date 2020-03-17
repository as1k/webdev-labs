def minf(a, b, c, d):
    return min(a, min(b, min(c, d)))


arr = [int(i) for i in input().split()]
print(minf(arr[0], arr[1], arr[2], arr[3]))
