import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import datetime

def getLList(L,L1,L2):
	"""
		opens gold_labels.txt and sorts all nodes into L1 or L2

	"""
	if not os.path.isfile("gold_labels.txt"):
		print "Gold labels missing ! Exitting"
		quit()

	goldy = open("gold_labels.txt",'r')
	text = goldy.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		L[node] = label
	
	for key in L:
		if L[key]=="L2":
			L2[key] = L[key]
		else:
			L1[key] = L[key]
	#print "The lists"
	#print L		
	#print L1
	#print L2


def getPredicted(Lp,L1p,L2p):
	"""
		go to label_prop_output.txt and get predicted values for labels
	"""
	if not os.path.isfile("label_prop_output.txt"):
		print "Output file missing ! Did you run junto for each part ? "
		quit()

	out = open("label_prop_output.txt",'r')
	text = out.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<3:
			continue
		node = each.split("\t")[0]
		# safe to assume that predicted label given first before dummy
		label_predict = each.split("\t")[3].split(" ")[0]
		predom_val = each.split("\t")[3].split(" ")[1]
		other_val = each.split("\t")[3].split(" ")[3]

		Lp[node] = label_predict
		if label_predict=="L2":
			L2p[node] = predom_val
			L1p[node] = other_val
		else:
			L1p[node] = predom_val
			L2p[node] = other_val

	"""for node in Lp:
		if Lp[node]=="L2" or Lp[node]=="L1":
			print "NODE :  ",node,"prediction : ",Lp[node]
		print "with L1 : ",L1p[node],"and L2 : ",L2p[node]
	"""
	L1prediction = 0
	L2prediction = 0
	#return the sizes
	for node in Lp:
		if Lp[node]=="L2":
			L2prediction += 1

		elif Lp[node]=="L1":
			L1prediction += 1

	return L1prediction,L2prediction
		


def  getIntersection(L,M,label):
	"""
		returns a dict containing elements present in both L and M
		consider label for differentiating
	"""
	common = dict()
	for key in L:
		if key not in M:
			continue
		elif M[key]!=label:
			continue
		else:
			common[key] = key;#the value of common[key] doesn't matter here

	return common


def analyzeForStep(STEPnum,partnum):
	"""
		run the process for each step
	"""
	os.chdir("STEP"+str(STEPnum)+"/part"+str(partnum)+"/")
	#print "dir : "+os.getcwd()
	Lg = dict()#The g stands for gold
	L1g = dict()
	L2g = dict()
	#go to gold_labels.txt and get our given lists
	getLList(Lg,L1g,L2g)

	Lp = dict()#p stands for prediction value
	L1p = dict()#L1 p and L2 p hold the predicted values 
	L2p = dict()#

	#go to label_prop_output
	L1predictnum,L2predictnum =  getPredicted(Lp,L1p,L2p)
	#print "prediction numbers : ",L1predictnum," and ",L2predictnum

	#print "The sizes are Lg :",len(Lg),"and Lp : ",len(Lp)
	L1common = getIntersection(L1g,Lp,"L1")
	L2common = getIntersection(L2g,Lp,"L2")

	#print "L1 common: ",L1common
	#print "L2 common: ",L2common

#report stats
	now = datetime.datetime.now()
	result_string = "+---\tResults for Step "+str(STEPnum)+" part "+str(partnum)+"---+"
	result_string += "\nResults as per "+now.strftime("%d-%m-%Y %H:%M")

	print result_string
#precision
	if L1predictnum!=0:
		precision1 = 100.0*len(L1common)/L1predictnum
		#print "L1 predictions : ",len(L1common)," common : : predicted ",L1predictnum
	else:
		precision1 = "NA"
	if L2predictnum!=0:
		precision2 = 100.0*len(L2common)/L2predictnum
		#print "L2 predictions : ",len(L2common)," common : : predicted ",L2predictnum
	else:
		precision2 = "NA"

	print "Precisions : ",precision1," and ",precision2
#recall
	if(len(L1g)!=0):
		recall1 = 100.0*len(L1common)/len(L1g)
	else:
		recall1 = "NA"
	if(len(L2g)!=0):
		recall2 = 100.0*len(L2common)/len(L2g)
	else:
		recall2 = "NA"	

	print "Recall : ",recall1," and ",recall2
#accuracy
	if(len(Lg)!=0):
		accuracy = 100.0*(len(L1common) + len(L2common))/len(Lg)
	else:
		accuracy = "NA"# Possible only when output not generated
	
	print "accuracy: ",accuracy


#Everything now calculated , now write this into a results folder

	#make connections between edges and their code names
	with open("nodes_dict.txt") as f:
		dic = json.loads(f.read())

		for each in dic:
			for x in dic[each]:
				print "N",each,"connects\t",x,"to",dic[each][x][0].split(" ")[0]





	os.chdir("../..")




#MAIN PART

#validate part
partnum = raw_input("Enter part num : ")
nope = (5,10,12,18,22,24)
partnum = int(partnum)

if partnum in range(1,31):
	if partnum in nope:
		print "This is an ignored part"
		quit()
else : 
	print "not even in range"

for STEPnum in range(1,2):#do for each STEP

	base_path = "STEP"+str(STEPnum)+"/part"+str(partnum)+"/"
	gold = "gold_labels.txt"
	out = "label_prop_output.txt"
	if not os.path.isfile(base_path+gold):
		print "Gold labels missing! ...Closing"
		quit()
	elif not os.path.isfile(base_path+out):
		print "Output file missing! ...Closing"
		quit()
	else:
		analyzeForStep(STEPnum,partnum)