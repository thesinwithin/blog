#/usr/bin/python

def make_bricks(small, big, goal):
  progress = 0
  for n in xrange(big):
    progress = progress+5
    print progress
    if progress == goal:
      print progress
      break
    if progress > goal:
      progress = progress - 5
      print progress
  if progress == goal:
    return True
  if progress < goal:
    for n in xrange(small):
      progress = progress + 1
      print progress
      if progress == goal:
        break
  if progress == goal:
    return True
  else:
    return False

