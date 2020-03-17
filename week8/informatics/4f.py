n = int(input())
a = [int(i) for i in input().split()]
s = 0
for f in range(1, n-1):
    if (a[f] > a[f-1]) & (a[f] > a[f+1]):
        s += 1
print(s)
