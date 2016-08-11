import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv

def getNodes():
	"""
		return a dict containing all nodes in gold labels
	"""
	filename="gold_labels.txt"
	if not os.path.isfile(filename):
		print filename,"missing ! Closing now..."
		quit()
	U = dict()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		U[node] = label
	filer.close()
	return U


def partRemoveCopy(partnum):
	"""
		loop on part number
	"""
	os.chdir("part"+str(partnum))

	U = getNodes()

	#open seeds and remove duplicate nodes
	duplicate_str = ""
	keep_str = ""
	filename = "seeds.txt"
	if not os.path.isfile(filename):
		print filename,"missing ! Closing now..."
		quit()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	for i in range(1,len(data)):
		each = data[i]
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]

		if node in U:
			duplicate_str+=each+"\n"
			print "Copy detected ->",each
		else:
			keep_str+=each+"\n"
	filer.close()

	dopple = open("duplicates.txt",'wb')
	dopple.write(duplicate_str)
	dopple.close()
	filer = open("seeds.txt",'wb')
	filer.write(keep_str)
	filer.close()
	
	print "Fixed part",partnum
	os.chdir("..")


def StepremoveCopy(STEPnum):
	"""
		loop for each step
	"""
	os.chdir("STEP"+str(STEPnum))
	nope = (5,10,12,18,22,24)
	for i in range(1,31):
		print "part",i,"\n"
		if i in nope:
			continue
		else:
			partRemoveCopy(i)

	os.chdir("..")


#main interface
print "This script will modify your seeds.txt file",
" to remove nodes appearing in gold_labels as well"
Proceed = raw_input("Continue ? y for yes : ")
if Proceed!='y':
	quit()

for STEPnum in range(1,4):
	print "STEP",STEPnum,"\n"
	StepremoveCopy(STEPnum)

