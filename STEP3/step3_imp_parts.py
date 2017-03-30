#!/usr/bin/env python
import graph
import merge
from shutil import copyfile
import os
import time

# same as simplify_loop_for3, but only generates output files,
# does not run junto

nope = (5,10,12,18,22,24)
# i is the iterator to run all parts
print '+--- Initiate Graph Generation ---+\n'
imp_part = (2,15,23,26,29)

for i in range(1,31):
	#part removed
	if i in imp_part:
		#use input for graph
		print '\nRunning part',i,'\n'
		graph.main(i)
		merge.main(i)
		print 'Part',i,'graph generated\n'

		time.sleep(0.5)
