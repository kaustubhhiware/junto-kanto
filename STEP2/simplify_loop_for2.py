#!/usr/bin/env python
import graph
from shutil import copyfile
import os

def juntofy(i):
	"""
		generate all outputs file
	"""
	#copy the simple_config to generate output
	copyfile("simple_config","part"+str(i)+"/simple_config")
	#go to each part
	os.chdir("part"+str(i))
	os.system("junto config simple_config")
	print '\noutput for part',i,'generated\n'
	#return to main STEP dir for next parts
	os.chdir("..")

nope = (5,10,12,18,22,24)
# i is the iterator to run all parts

for i in range(1,31):
	#part removed
	if i in nope:
		print '\npart',i,'ignored\n'
		continue
	else :
		#use input for graph
		print '\nRunning part',i,'\n'
		graph.main(i)
		print 'Part',i,'graph generated\n'

		juntofy(i)
		time.sleep(0.5)
