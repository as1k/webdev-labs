import math
a = float(input())
s = 2
for i in range(2, math.ceil(math.sqrt(a))):
    if a % i == 0:
        s += 2
if math.sqrt(a) == math.ceil(math.sqrt(a)):
    s += 1
print(s)
