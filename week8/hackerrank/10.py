n = int(input())
a = []
b = []
c = []

for i in range (0,n):
    a.append(str(input()))
    b.append(float(input()))

m1 = (min(b))
m2 = float(99999999999)

for i in range(0,n):
    if b[i] != m1 and b[i] < m2:
        m2 = b[i]

for i in range(0,n):
    if m2 == b[i]:
        name = a[i]
        c.append(name)

c.sort()
for i in range(0,len(c)):
    print(c[i])