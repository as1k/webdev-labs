a = int(input())
b = int(input())
if a == b:
    if a % 2 == 0:
        print(a)
else:
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=' ')
