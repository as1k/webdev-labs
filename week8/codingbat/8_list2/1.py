def count_evens(nums):
  cnt = 0
  for n in nums:
    if n % 2 == 0:
      cnt+=1
  return cnt
