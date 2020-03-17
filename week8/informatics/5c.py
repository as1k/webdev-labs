def xor(x, y):
    return x != y


a = [int(i) for i in input().split()]
if xor(a[0], a[1]):
    print(1)
else:
    print(0)
