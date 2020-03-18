def front_times(str, n):
  new_str = ""
  i = 0
  while i < n:
    if len(str) > 3:
      new_str += str[0:3]
    else:
      new_str += str
    i += 1
  return new_str