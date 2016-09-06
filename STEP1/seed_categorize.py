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
import csv
import io
import json

def standardize(set):
	"""
		format yes no not_sure to point to nodes
	"""
	for j in range(0,len(set)):
		set[j] = set[j][0]

	return set


def getList(i,L1,L2):
	"""
		opens seeds.txt and sorts all nodes into L1 or L2
	"""
	filename = "part"+str(i)+"/seeds.txt"
	if not os.path.isfile(filename):
		print "Seeds.txt missing ! Exitting"
		quit()

	goldy = open(filename,'r')
	text = goldy.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		key = each.split("\t")[0]
		label = each.split("\t")[1]

		if label=="L1":
			L1[key] = key
		elif label=="L2":
			L2[key] = key

	goldy.close()


def countFrom(L,yes,no,not_sure):

	vruddhiNum = 0
	nonvruddhiNum = 0
	confusedNum = 0
	
	for key in L:
		if key in yes:
			vruddhiNum += 1
		elif key in no:
			nonvruddhiNum += 1
		elif key in not_sure:
			confusedNum += 1

	return vruddhiNum,nonvruddhiNum,confusedNum

if __name__=="__main__":

	to_run = (2,15,23,26,29)
	separate_exe = {'2':part2,'15':part15,'23':part23,'26':part26,'29':Step1}
	imp_part = (2,15,23,26,29)

	# i is the iterator to run all parts
	seeds_data = [['Part#','>>','Vruddhi','>>','Non vruddhi','>>','Confused','+------','Total','------+','Total']]
	seeds_data.append([' ','L1','L2','L1','L2','L1','L2','Vruddhi','NV','Confused','Seeds'])

	count_list = []
	yes = []
	no = []
	not_sure = []
	i = 1
	for i in to_run:
		i = 2
		print '\n+--- Running for part',i,'\n'
		#count list is not needed here , just for completion sake
		count_list,yes,no,not_sure = separate_exe[str(i)].main_new(1)
		with io.open("part2_yes.json", "w", encoding="utf8") as ft:
			ft.write(unicode(json.dumps(yes,indent=4,ensure_ascii=False,sort_keys=True)))
		yes = standardize(yes)
		no = standardize(no)
		not_sure = standardize(not_sure)	

		L1 = dict()
		L2 = dict()
		getList(i,L1,L2)

		#with io.open('../results/step1_part2.json','wb',encoding="utf8") as csvfile:
		#	json.dump(yes,csvfile,indent=4,ensure_ascii=False,sort_keys=True)
	#	with open("test.txt", "w") as f:
	#	    f.write(yes)


		vruddhiL1,nonvruddhiL1,confusedL1 = countFrom(L1,yes,no,not_sure)
		vruddhiL2,nonvruddhiL2,confusedL2 = countFrom(L2,yes,no,not_sure)

		tots = 0
		tots += vruddhiL1+vruddhiL2+nonvruddhiL1+nonvruddhiL2+confusedL1+confusedL2
		seeds_data.append([i,vruddhiL1,vruddhiL2,nonvruddhiL1,nonvruddhiL2,confusedL1,confusedL2,len(yes),len(no),len(not_sure),tots])
		exit()

	print 'Writing now'
	#print seeds_data
	with open('../results/step1_seedsVruddhi.csv','wb') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in seeds_data : 
			 writer.writerow(eachrow)