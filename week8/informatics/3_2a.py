import math
n = int(input())
i = 1
while i <= n:
    if math.sqrt(i) == math.ceil(math.sqrt(i)):
        print(i)
    i += 1