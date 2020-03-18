def lucky_sum(a, b, c):
  sum = 0
  if a == 13:
    return 0
  if b == 13 and a != 13:
    return sum+a
  if c == 13 and a != 13 and b != 13:
    return sum + a + b
  else:
    return sum + a + b + c
