#!/usr/bin/env python
import os
import simply_copy
from shutil import copyfile
import time
import hunt_duplicates


def build_junto():
	#compile junto once
	junto_loc = os.environ['JUNTO_DIR']
	time.sleep(0.5)
	print 'Need to compile junto for first time at',junto_loc
	come_back_to = os.getcwd()
	os.chdir(junto_loc)
	time.sleep(0.5)
	print 'bin/build update compile'
	os.system("bin/build update compile")
	print 'back to location...'
	os.chdir(come_back_to)
	time.sleep(2)

def part1():
	#copy simple_config to STEP1 for simplify_looper
	# custom made config file
	copyfile("simple_config","STEP1/simple_config")
	#go to STEP1 first
	os.chdir("STEP1")
	#print("Path at terminal when executing this file")
	curr_loc = os.getcwd()
	#print 'Permission'
	init_file = curr_loc+'/simplify_looper.py'#declare location

	print '\n+++--- Starting STEP1 ---+++\n'
	os.chmod(init_file,0755)#mark executable first
	os.system(init_file)
	print 'all parts in step 1 outputs have been built!'
	time.sleep(2)	
	os.chdir("..")


def part2():

	#go to Step 2 and its file for further actions
	copyfile("simple_config","STEP2/simple_config")
	os.chdir("STEP2")
	curr_loc = os.getcwd()
	sec_file = curr_loc+'/simplify_loop_for2.py'

	print '\n+++--- Starting STEP2 ---+++\n'
	os.chmod(sec_file,0755)#mark executable first
	os.system(sec_file)
	print 'all parts in step 2 outputs have been built!'
	time.sleep(2)
	os.chdir("..")

k = raw_input("Build junto once ? Enter y for building : ")
if k=="y":
	build_junto()

#is_first = raw_input("Build part 1 ? y for yes : ")
#if is_first=="y":
#	part1()
part1()

print '\n+--- Copying all output files to STEP 2---+\n'
simply_copy.copy(1)

#is_second = raw_input("Build part 2 ? y for yes : ")
#if is_second:
#	part2()
part2()
print '\n+--- Copying all output files to STEP 3---+\n'
simply_copy.copy(2)

#go to Step 3 and its file for further actions
copyfile("simple_config","STEP3/simple_config")
os.chdir("STEP3")
curr_loc = os.getcwd()
ter_file = curr_loc+'/simplify_loop_for3.py'

print '\n+++--- Starting STEP3 ---+++\n'
os.chmod(ter_file,0755)#mark executable first
os.system(ter_file)
print 'all parts in step3 outputs have been built!'
time.sleep(2)

