#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p174314
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) == len(b):
    if a == b:
      return True
    else:
      return False
  if len(a) > len(b):
    if a.endswith(b):
      return True
    else:
      return False
  if len(a) < len(b):
    if b.endswith(a):
      return True
    else:
      return False
