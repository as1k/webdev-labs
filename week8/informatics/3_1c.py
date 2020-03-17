import math
a = int(input())
b = int(input())
for i in range (a, b+1):
    if math.sqrt(i) == math.ceil(math.sqrt(i)):
        print(i, end=' ')
