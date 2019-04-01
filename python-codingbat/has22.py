#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p119308
def has22(nums):
  for idx in xrange(len(nums)-1):
    if nums[idx] == 2 and nums[idx+1] == 2:
      return True
  return False
