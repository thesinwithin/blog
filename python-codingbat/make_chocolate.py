#/usr/bin/python
# the problem definition can be found at https://codingbat.com/prob/p190859

def make_chocolate(small, big, goal):
	progress = 0
	bars = 0
	for n in xrange(big):
		progress = progress+5
		if progress == goal:
			break
		if progress > goal:
		progress = progress - 5
	if progress == goal:
		return 0
	if progress < goal:
		for n in xrange(small):
			progress = progress + 1
			bars = bars + 1
			if progress == goal:
				break
	if progress == goal:
		return bars
	else:
		return -1
