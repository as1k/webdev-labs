def pos_neg(a, b, negative):
  if (a < 0) and (b > 0) and (negative is False) or (a > 0) and (b < 0) and (negative is False):
    return True
  elif (a < 0) and (b < 0) and (negative is True):
    return True
  else:
    return False