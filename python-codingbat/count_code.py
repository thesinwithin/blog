#/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p186048
def count_code(str):
  advance = 0
  matches = 0
  for i in xrange(len(str)):
    try:
      if str[advance] == 'c' and str[advance+1] == 'o' and str[advance+3] == 'e':
        matches = matches + 1
      advance = advance + 1
    except:
      pass
  return matches
