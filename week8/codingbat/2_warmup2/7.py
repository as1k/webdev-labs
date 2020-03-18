def array_count9(nums):
  cnt = 0
  for i in range(0, len(nums)):
    if nums[i] == 9:
      cnt += 1
  return cnt