n = int(input())
a = [int(i) for i in input().split()]
for f in range(0, n//2):
    c = a[f]
    a[f] = a[n-f-1]
    a[n-f-1] = c
for f in range(0, n):
    print(a[f], end=' ')
