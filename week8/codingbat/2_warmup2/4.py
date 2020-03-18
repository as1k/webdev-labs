def string_splosion(str):
  result = ""
  for i in range(0, len(str)):
    result += str[:i+1]
  return result