import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
from prettytable import PrettyTable
import time

def  getUnion(L,M,prnt=0):
	"""
		returns a dict containing elements present in both L and M
	"""
	unite = dict()
	for key in L:
		unite[key] = key#the value of common[key] doesn't matter here
		
	for element in M:
		if element not in unite:
			unite[element] = element
	
	if(prnt):
		print 'aasavenya  : length : ',len(unite)
		print 'L : ',len(L)
		print 'M : ',len(M)
	return unite


def getCountFrom(filename):
	"""
		open that file and return count of nodes in both label
		U holds all the unique nodes across all countFrom's
	"""

	if not os.path.isfile(filename):
		print filename,"missing ! Closing now..."
		quit()
	U = dict()
	countL1 = 0
	countL2 = 0
	countAll = 0
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		if node not in U:
			countAll += 1
		U[node] = node

		if label=="L1":
			countL1 += 1
		else :#obviously , should be L2
			countL2 += 1

	filer.close()
	return countL1,countL2,countAll,U



def InputNodes():
	"""
		open input_graph.txt and return count of nodes
	"""
	filename="input_graph.txt"

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
		n1 = each.split("\t")[0]
		n2 = each.split("\t")[1]
		U[n1] = n1
		U[n2] = n2

	filer.close()
	return U

def getNodesFromPart(i,data):
	"""
		get nodes from part i
	"""
	os.chdir("part"+str(i))
	print "+---\tNodes in part ",str(i),"\t---+\n\n"
	time.sleep(0.6)
	seednode = dict()
	goldnode = dict()
	L1seed,L2seed,seeds,seednode = getCountFrom("seeds.txt")
	L1gold,L2gold,golds,goldnode = getCountFrom("gold_labels.txt")
	Unique = dict()

	Unique = getUnion(goldnode,seednode)
	graphnode = InputNodes()
	#print Unique
	
	for each in Unique:
		if each not in graphnode:
			print each,"Traitor"
			time.sleep(0.5)


	os.chdir("..")
	return data


print "Checking if format available.... "
os.system("pip install PrettyTable")

STEPnum = raw_input("Enter step number for which node analysis is required : ")
STEPnum = int(STEPnum)
if STEPnum not in range(1,4):
	print "Not valid"
	quit()

dataHolder = dict()
os.chdir("STEP"+str(STEPnum))

out_string = "+---\tNodes in Step "+str(STEPnum)+"\t---+\n\n"
print out_string
nope = (5,10,12,18,22,24)
for i in range(1,31):
	if i in nope:
		continue
	else:
		dataHolder = getNodesFromPart(i,dataHolder)

