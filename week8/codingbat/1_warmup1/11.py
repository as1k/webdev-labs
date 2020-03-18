def front_back(str):
  n = len(str)
  if n>=2:
    new_str = str[-1:] + str[1:-1] + str[:1]
  else:
    return str
  return new_str