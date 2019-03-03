#/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p118406
def make_bricks(small, big, goal):
  progress = 0
  for n in xrange(big):
    progress = progress+5
    if progress == goal:
      break
    if progress > goal:
      progress = progress - 5
  if progress == goal:
    return True
  if progress < goal:
    for n in xrange(small):
      progress = progress + 1
      if progress == goal:
        break
  if progress == goal:
    return True
  else:
    return False
