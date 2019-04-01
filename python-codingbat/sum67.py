#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p108886

def sum67(nums):
  if len(nums) == 0:
    return 0
  idx = 0
  s = 0
  while idx < len(nums):
    if nums[idx] == 6:
      while nums[idx] != 7:
        idx += 1
      idx += 1
    if idx < len(nums) and nums[idx] != 6:  
      s += nums[idx]
      idx +=1
  return s
