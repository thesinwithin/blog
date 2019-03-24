#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p189616 
def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0 :
      count += 1
  return count

