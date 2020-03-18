def array123(nums):
  if len(nums)<3:
    return False
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      result = True
      break
    else:
      result = False
  return result