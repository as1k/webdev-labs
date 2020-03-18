def string_match(a, b):
  r = len(a) if len(a)<len(b) else len(b)
  result = 0
  for i in range(r):
    if a[i:i+2] == b[i:i+2] and len(a[i:i+2]) == 2 and len(b[i:i+2]) == 2:
      result += 1
  return result