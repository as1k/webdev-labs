n = int(input())
s = 0
i = [int(a) for a in input().split()]
for f in range(0, n):
    if i[f] > 0:
        s += 1
print(s)
