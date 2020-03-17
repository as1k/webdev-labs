a = int(input())
if (a % 4 == 0) & (a % 100 != 0) | (a % 400 == 0):
    print('YES')
else:
    print('NO')
