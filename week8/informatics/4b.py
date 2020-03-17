n = int(input())
a = [int(i) for i in input().split()]
for f in range(0, n):
    if a[f] % 2 == 0:
        print(a[f], end=' ')
