#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p167025
def sum13(nums):
  if len(nums) == 0:
    return 0
  idx = 0
  
  while idx < len(nums):
      if nums[idx] == 13:
          del nums[idx:idx+2]
          continue
      idx += 1
  return sum(nums)
