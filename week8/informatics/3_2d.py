n = int(input())
pow = 1
ans = 0
while pow <= n:
    if pow == n:
        ans = 1
        break
    pow *= 2
if ans == 0:
    print('NO')
else:
    print('YES')