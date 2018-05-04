#!/usr/local/bin/python3.6

import itertools
import json
import re

d=dict([])

file_in = open("input.txt","r")
input = file_in.read()
halves = input.split('\n\n')

for i in xrange(0,len(halves)-1):
	k=[]
	v=[]
	for line in itertools.islice(halves[i].split('\n'),3,None):
		a=line.split('|')
		k.append(a[0].strip())
		v.append(a[1].strip())
	d['PSU%i' %i] = dict(zip(k, v))

for i in xrange(0,len(halves)-1):
	d['PSU%i' %i]['Temperature 1'] = d['PSU%i' %i]['Temperature 1'].split('/')[0][:-1]
	d['PSU%i' %i]['Temperature 2'] = d['PSU%i' %i]['Temperature 2'].split('/')[0][:-1]
	d['PSU%i' %i]['Input Current'] = d['PSU%i' %i]['Input Current'][:-2]
	d['PSU%i' %i]['Input Power'] = d['PSU%i' %i]['Input Power'][:-2]
	d['PSU%i' %i]['Input Voltage'] = d['PSU%i' %i]['Input Voltage'][:-2]
	d['PSU%i' %i]['Main Output Current'] = d['PSU%i' %i]['Main Output Current'][:-2]
	d['PSU%i' %i]['Main Output Power'] = d['PSU%i' %i]['Main Output Power'][:-2]
	d['PSU%i' %i]['Main Output Voltage'] = d['PSU%i' %i]['Main Output Voltage'][:-2]
	d['PSU%i' %i]['Fan 1'] = d['PSU%i' %i]['Fan 1'][:-4]
	d['PSU%i' %i]['Fan 2'] = d['PSU%i' %i]['Fan 2'][:-4]	
	
	v = re.search(r'(\[\w+ \w+\])\(\w+\)', d['PSU%i' %i]['Status']).group(1)
	d['PSU%i' %i]['Status'] = ''.join(c for c in v if c not in '[]')[7:]

	d['PSU%i' %i].pop('PMBus Revision', None)
	d['PSU%i' %i].pop('PWS Module Number', None)
	d['PSU%i' %i].pop('PWS Revision', None)
	d['PSU%i' %i].pop('PWS Serial Number', None)

print(json.dumps(d, sort_keys=True,indent=4,separators=(',', ': ')))
