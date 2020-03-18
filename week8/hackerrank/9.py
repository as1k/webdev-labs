n = int(input())
b = input().split()
arr = []

for i in range (0,n):
    arr.append(int(b[i]))

m1 = int(max(arr))
m2 = int(-100)

for i in range(0,n):
    if arr[i] != m1 and arr[i] > m2:
        m2 = arr[i]

print(m2)