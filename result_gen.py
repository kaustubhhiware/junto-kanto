import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import datetime
from prettytable import PrettyTable
import time

def nodesFrom(filename,U):
	"""
		open that file and add nodes to U
	"""

	if not os.path.isfile(filename):
		print filename,"missing ! Closing now..."
		quit()

	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		U[node] = node

	filer.close()


def createUniversal():
	"""
		add all nodes worth considering to a dict to be used later
	"""
	U = dict()
	nodesFrom("gold_labels.txt",U)
	nodesFrom("seeds.txt",U)
	#print "\nI matter : \n",U
	return U


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

	goldy.close()
	#print "The lists"
	#print L		
	#print L1
	#print L2


def getPredicted(Lp,L1p,L2p,U):
	"""
		go to label_prop_output.txt and get predicted values for labels
		a node is stored only if it is in the relevant set U
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
		if node in U:
			Lp[node] = label_predict
			#print type(label_predict),"Type hai\n"
			if label_predict=="L2":
				L2p[node] = predom_val
				L1p[node] = other_val
			elif label_predict=="L1":
				L1p[node] = predom_val
				L2p[node] = other_val
		#else:
		#	print node,"not relevant\n"
	"""
	for node in Lp:
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

	out.close()
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
			common[key] = key#the value of common[key] doesn't matter here

	return common

def allcounts(L1g,L2g,Lg,Lp):
	"""
		classify all nodes for computation
	"""
	# consider only those nodes whose output is known
	givenL1predictL1 = 0
	givenL1predictL2 = 0
	givenL2predictL1 = 0
	givenL2predictL2 = 0

	for key in Lg :
		if key in Lp:
			if key in L1g:
				if Lp[key]=="L1":
					givenL1predictL1 += 1
				elif Lp[key]=="L2":
					givenL1predictL2 += 1
			elif key in L2g:
				if Lp[key]=="L1":
					givenL2predictL1 += 1
				elif Lp[key]=="L2":
					givenL2predictL2 += 1
				time.sleep(0.5)

	return givenL1predictL1,givenL1predictL2,givenL2predictL1,givenL2predictL2


def analyzeForStep(STEPnum,partnum):
	"""
		run the process for each step
	"""
	os.chdir("STEP"+str(STEPnum)+"/part"+str(partnum)+"/")
	#print "dir : "+os.getcwd()

	#first , generate a universal set comprising of nodes in seeds and gold_labels
	#rest are to be skipped
	U = createUniversal()

	Lg = dict()#The g stands for gold
	L1g = dict()
	L2g = dict()
	#go to gold_labels.txt and get our given lists
	getLList(Lg,L1g,L2g)

	Lp = dict()#p stands for prediction value
	L1p = dict()#L1 p and L2 p hold the predicted values 
	L2p = dict()#
	#print "\nI matter : \n",U
	#go to label_prop_output
	L1predictnum,L2predictnum =  getPredicted(Lp,L1p,L2p,U)
	#print "prediction numbers : ",L1predictnum," and ",L2predictnum

	#print "The sizes are Lg :",len(Lg),"and Lp : ",len(Lp)
	#L1common = getIntersection(L1g,Lp,"L1")
	#L2common = getIntersection(L2g,Lp,"L2")
	#print "L1 common: ",L1common
	#print "L2 common: ",L2common

	print'+--- Computing...'
	givenL1predictL1,givenL1predictL2,givenL2predictL1,givenL2predictL2 = allcounts(L1g,L2g,Lg,Lp)
	print "Stats"
	print givenL1predictL1,givenL1predictL2,givenL2predictL1,givenL2predictL2 

#report stats
	now = datetime.datetime.now()
	result_string = "+---\tResults for Step "+str(STEPnum)+" part "+str(partnum)
	result_string += "\t---+\n\n"
	result_string += "\nResults as compiled on "+now.strftime("%d-%m-%Y %H:%M")+"\n\n"

	print result_string

	statsTable = PrettyTable(['Detail','L1','L2'])
#precision
	if ((givenL1predictL1+givenL1predictL2)!=0):
		precision1 = 100.0*givenL1predictL1/(givenL1predictL1+givenL1predictL2)
		#print "L1 predictions : ",len(L1common)," common : : predicted ",L1predictnum
		precision1 = 0.001 * int(1000*precision1)
	else:
		precision1 = "-"
	if ((givenL2predictL1+givenL2predictL2)!=0):
		precision2 = 100.0*givenL2predictL2/(givenL2predictL1+givenL2predictL2)
		#print "L2 predictions : ",len(L2common)," common : : predicted ",L2predictnum
		precision2 = 0.001 * int(1000*precision2)
	else:
		precision2 = "-"

#	print "Precisions : ",precision1," and ",precision2
	statsTable.add_row(['Precision',precision1,precision2])
#recall
	if ((givenL1predictL1+givenL2predictL1)!=0):
		recall1 = 100.0*givenL1predictL1/(givenL1predictL1+givenL2predictL1)
		recall1 = 0.001 * int(1000*recall1)
	else:
		recall1 = "-"
	if ((givenL1predictL2+givenL2predictL2)!=0):
		recall2 = 100.0*givenL2predictL2/(givenL1predictL2+givenL2predictL2)
		recall2 = 0.001 * int(1000*recall2)
	else:
		recall2 = "-"	

#	print "Recall : ",recall1," and ",recall2
	statsTable.add_row(['Recall',recall1,recall2])

#accuracy
	if((givenL1predictL2+givenL2predictL2+givenL1predictL1+givenL2predictL1)!=0):
		accuracy = 100.0*(givenL1predictL1+givenL2predictL2)
		accuracy /= (givenL1predictL2+givenL2predictL2+givenL1predictL1+givenL2predictL1)
		accuracy = 0.001 * int(1000*accuracy)
	else:
		accuracy = "-"# Possible only when output not generated

#	print "accuracy: ",accuracy
	statsTable.add_row(['Accuracy','=>',accuracy])

	stats_text = statsTable.get_string()
	#print stats_text
	result_string += "\n"+stats_text+"\n"

#Everything now calculated , now write this into a results folder

	label_data = [['Node','Mapping','Goldlabel','Predict',
		'L1 confidence','L2confidence']]
	connectionTable = PrettyTable(['Node','Mapping','Goldlabel','Predict',
		'L1 confidence','L2confidence'])
	#make connections between edges and their code names
	with open("nodes_dict.txt") as f:
		dic = json.loads(f.read())

		for each in dic:
			for x in dic[each]:
				#print "N",each," :",x,"->",
				#dic[each][x][0].split(" ")[0],"L1",L1p["N"+each],"L2",L2p["N"+each]
				index = "N"+each
				if index not in U:
					continue
				mapping = x+"->"+dic[each][x][0].split(" ")[0]
				if index in Lg:
					given = Lg[index]
				else:
					given = "-"

				if index in Lp:
					predicted = Lp[index]
					if predicted!="__DUMMY__":
						L1val = 0.001 * int( 1000 * float(L1p[index]))
						L2val = 0.001 * int( 1000 * float(L2p[index]))
				else:
					predicted = "-"
					L1val = "-"
					L2val = "-"

				connectionTable.add_row([index,mapping,given,predicted,L1val,L2val])
				label_data.append([index,mapping,given,predicted,L1val,L2val])
	connections = connectionTable.get_string()
	#print connections
	result_string += "\n"+connections+"\n"

	os.chdir("../..")
	os.system("mkdir results")
	outstr = "results/step_"+str(STEPnum)+"_part_"+str(partnum)+"_.txt"
	

	with open('results/step'+str(STEPnum)+"_part_"+str(partnum)+'_results.csv','wb') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in label_data : 
			 writer.writerow(eachrow)

	if os.path.isfile(outstr):
		os.system("rm -f "+outstr)
		print "Updating results ..."

	outFile = open(outstr,'wb')		
	outFile.write(result_string)
	outFile.close()




#MAIN PART
if __name__=="__main__":
	#validate part
	print "Checking if format available.... "
	os.system("pip install PrettyTable")

	partnum = raw_input("Enter part num : ")
	nope = (5,10,12,18,22,24)
	partnum = int(partnum)

	if partnum in range(1,31):
		if partnum in nope:
			print "This is an ignored part"
			quit()
	else : 
		print "not even in range"

	STEPnum = raw_input("Enter which Step : ")
	STEPnum = int(STEPnum)
	if STEPnum not in range(1,4):
		print "Not valid"
		quit()

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