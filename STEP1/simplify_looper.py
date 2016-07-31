#!/usr/bin/env python
import Step1
import part2
import part4
import part15
import part19
import part23
import part26
import time
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

run_separate = (2,4,15,19,23,26)
separate_exe = {'2':part2,'4':part4,'15':part15,'19':part19,'23':part23,'26':part26}
nope = (5,10,12,18,22,24)
# i is the iterator to run all parts

for i in range(1,31):
	#part removed
	if i in nope:
		print '\npart',i,'ignored\n'
		continue
	# textbook
	elif i not in run_separate :

		#use input for graph
		print '\nRunning part',i,'\n'
		Step1.run(i)
		print 'Part',i,'graph generated\n'

		juntofy(i)
		time.sleep(0.5)

	#separate run
	else :
		print '\nRunning part',i,'\n'
		separate_exe[str(i)].main_new()	
		print 'part',i,'graph generated\n'

		juntofy(i)
		time.sleep(0.5)