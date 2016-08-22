import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import time

def getNodes(filename):
	"""
		return a dict containing all nodes in gold labels
	"""
	#filename="gold_labels.txt"
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


def getLabels(label):
	"""
		return number of nodes with that label
	"""
	count = 0
	filename="seeds.txt"
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
		thisLabel = each.split("\t")[1]
		if thisLabel==label:
			count += 1

	filer.close()
	return count

def keepNumof(maximum,restrictLabel):
	"""
		keep only maximum number of nodes with Label
	"""
	counter = maximum
	filename= "seeds.txt"
	keep_str = ""
	duplicate_str = ""
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
		thisLabel = each.split("\t")[1]

		if thisLabel == restrictLabel and counter>0:
			counter -= 1
			keep_str+=each+"\n"
			#ignore first counter number of majority labels
		
		elif thisLabel == restrictLabel and counter < 1:
			duplicate_str+=each+"\n"
			print "Surplus ->",each
			counter -= 1
		else:
			keep_str+=each+"\n"
	filer.close()

	dopple = open("surplus_nodes.txt",'wb')
	dopple.write(duplicate_str)
	dopple.close()
	filer = open("seeds.txt",'wb')
	filer.write(keep_str)
	filer.close()


def equalizeNodes():
	"""
		ensure #L1 = #L2 in current part
	"""
	L1num = getLabels("L1")
	L2num = getLabels("L2")
	print "\n---",L1num,"\t---\t",L2num,"\n"

	if L1num < L2num:
		keepNumof(L1num,"L2")
	else:#if L2num > L1num:
		keepNumof(L2num,"L1")


def partRemoveCopy(partnum):
	"""
		loop on part number
	"""
	os.chdir("part"+str(partnum))

	U1 = getNodes("gold_labels.txt")
	U2 = getNodes("seeds.txt")

	U = U1
	if len(U2) < len(U1):
		U = U2

	correct_file = "seeds.txt"
	if len(U2) < len(U1):
		correct_file="gold_labels.txt"	
	#open seeds and remove duplicate nodes
	duplicate_str = ""
	keep_str = ""
	filename = correct_file
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
	filer = open(correct_file,'wb')
	filer.write(keep_str)
	filer.close()
	
	time.sleep(1)
	print 'Now equalizing labels'
	equalizeNodes()

	print "Fixed part",partnum
	os.chdir("..")


def StepremoveCopy(STEPnum):
	"""
		loop for each step
	"""
	#os.chdir("STEP"+str(STEPnum))
	nope = (5,10,12,18,22,24)
	for i in range(1,31):
		print "part",i,"\n"
		if i in nope:
			continue
		else:
			partRemoveCopy(i)

	#os.chdir("..")


#main interface
if __name__=="__main__":
	print "This script will modify your seeds.txt file",
	" to remove nodes appearing in gold_labels as well"
	Proceed = raw_input("Continue ? y for yes : ")
	if Proceed!='y':
		quit()

	# Not required as seeds in next steps are generated later
	#for STEPnum in range(1,4):
	#	print "STEP",STEPnum,"\n"
	#	StepremoveCopy(1)

	StepremoveCopy(1)
