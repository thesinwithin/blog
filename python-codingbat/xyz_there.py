#!/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p149391
def xyz_there(str):
  if 'xyz' in str:
    if '.xyz' in str:
      if str.count('xyz') == str.count('.xyz'):
        return False
      else:
        return True
    else:
      return True
  else:
    return False
