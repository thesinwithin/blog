#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p184853
def big_diff(nums):
  nums.sort()
  if len(nums) == 1:
    return 0
  else:
    return int(str(nums[-1])) - int(str(nums[0]))
