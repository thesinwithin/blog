#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p126968
def centered_average(nums):
  nums.sort()
  del nums[0]
  del nums[-1]
  if len(nums) == 1:
    return int(str(nums[0]))
  else:
    s = 0
    for n in nums:
      s = s + n
    return s / len(nums)
