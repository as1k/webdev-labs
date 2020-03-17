n = int(input())
a = [int(i) for i in input().split()]
for i in range(0, n, 2):
    print(a[i], end=' ')
