#!/usr/bin/env python
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import os

def edgesInPart(index):
	"""
		returns number of edges in input graph
	"""
	os.chdir("part"+str(index))
	filer = open("input_graph.txt",'r')
	text = filer.read()
	data = text.split("\n")
	
	#if index==29:
	#	print data
	os.chdir("..")
	return len(data)


def combinations(index,node_dict,dic,count,vruddhi,ends_with,two_vowels,last_second,total,count_list,seed_analyze=0):
	string = ""
	seeds_string = ""

	s_vow = ["a","e","i","o","u","f","U","I"]
	l_vow = ["A","E","O","F"]
	
	Error = []
	x = 0
	errors = 0
	fish = 0	
	count_num = [0,0,0]
	
	yes = []
	no = []
	not_sure = []

	count_0 = 0
	count_1 = 0
	report = 0


	for key in dic:
		for each in dic[key]:
			result = [0,0,0,0]
			temp = 0
			check = 100
			if len(each.split(" "))>2:
				continue
			elif len(each.split(" "))==2:
				source = each.split(" ")[0]
			else:
				source = each
			derived = key
			vowel_count = 0
			
			if two_vowels:
				for char in source:
					if char in l_vow or char in s_vow:
						vowel_count += 1
				if vowel_count == 2:
					result[2] = 1
			else:
				result[2] = 0
			
			if last_second != "":
				try:
					if source[-2] == last_second:
						result[3] = 1
					else:
						result[3] = 0
				except IndexError:
					result[3] = 0
				
			else:
				result[3] = 0

			if len(source)<=2:
				continue

			while(temp<len(source)):
				if source[temp] in s_vow:
					if source[temp] == "a":
						if derived[temp] == "A":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "e" or source[temp] == "i" or source[temp] == "I":
						if derived[temp] == "E":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "u" or source[temp] =="o" or source[temp] == "U":
						if derived[temp] == "O":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "f":
						if derived[temp:temp+2] == "Ar":
							check = 1
							break
						else:
							check = 0
							break
				elif source[temp] in l_vow:
					if derived[temp]==source[temp]:
						check = -1
					else:
						check = 0
					break
				temp += 1
				if temp>=len(source):
					break

			if type(vruddhi) == bool:
				if check == 1:
					if vruddhi == True:
						ans = 1
					else:
						ans = 0
				elif check == 0:
					if vruddhi == True:
						ans = 0
					else:
						ans = 1
				elif check == -1:
					ans = -1
				elif check == 100:
					continue
			else:
				ans = check			

			if len(ends_with)>0:
				if str(source)[len(source)-1] in ends_with:
					result[1] = 1
				else:
					result[1] = 0
			else:
				result[1] = 0

			if len(each.split(" "))>1:
				if int(each.split(" ")[1]) == 0:
					count_0 += 1
				elif int(each.split(" ")[1]) == 1:
					count_1 += 1
				else:
					print "WTF"
				seeds_string += "N"+str(count+x)+'\t'+"L"+str(int(each.split(" ")[1])+1)+'\t'+"1.0\n"
			else:
				if vruddhi == True and check == 0:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1
				if vruddhi == False and check == 1:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1

			result[0] = 1
			temp_node_list = []
			temp_node_list.append("N"+str(count+x))
			temp_node_list.append(result)
	
			if ans == 1:
				yes.append(temp_node_list)
			elif ans == 0:
				no.append(temp_node_list)
			elif ans == -1:
				not_sure.append(temp_node_list)

			temp_dic = {}
			temp_dic[key] = [each,result]
			node_dict[x+count] = temp_dic
			x+=1

	setG = dict()
	filer = open("part15/gold_labels.txt",'r')
	text = filer.read()
	data = text.split("\n")
	#print data
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		setG[node] = label
	#print "setG",setG

	setS = {}
###	Generate set for seeds
	
	data = seeds_string.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		#U[node] = label
		if node not in setG:
			setS[node] = label

###	
	edgeVSG = 0
	edgeVSUL = 0
	edgenVSG = 0
	edgenVSUL = 0

	for i in range(len(yes)):
		for j in range(i+1,len(yes)):
			weight = 0
			for k in range(4):
				if yes[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += yes[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"

			if yes[i][0] in setG and yes[j][0] in setS:
				edgeVSG += 1
			elif yes[i][0] in setS and yes[j][0] in setG:
				edgeVSG += 1

			# vruddhi unlabeled and seeds
			if yes[i][0] not in setG and yes[i][0] not in setS and yes[j][0] in setS:
				edgeVSUL += 1
			elif yes[i][0] in setS and yes[j][0] not in setG and yes[j][0] not in setS:
				edgeVSUL += 1

	for i in range(len(no)):
		for j in range(i+1,len(no)):
			weight = 0
			for k in range(4):
				if no[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += no[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"

			if no[i][0] in setG and no[j][0] in setS:
				edgenVSG += 1
			elif no[i][0] in setS and no[j][0] in setG:
				edgenVSG += 1

			if no[i][0] not in setG and no[i][0] not in setS and no[j][0] in setS:
				edgenVSUL += 1
			elif no[i][0] in setS and no[j][0] not in setG and no[j][0] not in setS:
				edgenVSUL += 1


	edgeCSG = 0 	# confused nodes
	edgeCSUL = 0

	for i in range(len(not_sure)):
		for j in range(i+1,len(not_sure)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and not_sure[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += not_sure[i][0]+'\t'+not_sure[j][0]+'\t'+str(weight)+"\n"
			
			if not_sure[i][0] in setG and not_sure[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and not_sure[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and not_sure[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and not_sure[j][0] not in setG and not_sure[j][0] not in setS:
				edgeCSUL += 1

	for i in range(len(not_sure)):
		for j in range(len(yes)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			string += not_sure[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"

			if not_sure[i][0] in setG and yes[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and yes[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and yes[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and yes[j][0] not in setG and yes[j][0] not in setS:
				edgeCSUL += 1
							
		for j in range(len(no)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			if weight<0:
				print "**** ERROR ****"
			string += not_sure[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"

			if not_sure[i][0] in setG and no[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and no[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and no[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and no[j][0] not in setG and no[j][0] not in setS:
				edgeCSUL += 1
	
	num_vruddhi = 0
	not_vruddhi = 0
	if vruddhi == True or type(vruddhi)!=bool:
		num_vruddhi = len(yes)
	elif vruddhi == False:
		num_vruddhi = len(no)
	if vruddhi == True or type(vruddhi)!=bool:
		not_vruddhi = len(no)
	elif vruddhi == False:
		not_vruddhi = len(yes)
	not_sure_vruddhi = len(not_sure)
	count += x
	
	count_list = ["part"+str(index),count_0,count_1,count-1,num_vruddhi,not_vruddhi,not_sure_vruddhi,len(string.split("\n"))]
		
	return edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,len(string.split("\n"))		
				

def main(n,vruddhi,ends_with,two_vowels,last_second,total,count_list):
	count = 1

	node_dict = defaultdict(lambda : defaultdict(lambda : str))
	input_dict = defaultdict(lambda : defaultdict(lambda : list()))
	with open("part"+str(n)+"/"+"part"+str(n)+"_algo_file.txt") as f:
		input_dict = json.loads(f.read())

	for key in input_dict:
		edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge = combinations(n,node_dict,input_dict[key],count,vruddhi,ends_with,two_vowels,last_second,total,count_list)


	print "part",n,"done"
	return edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge	

#(index,node_dict,dic,count,vruddhi,ends_with,two_vowels,last_second,total,count_list):
def main_new():

	counter = []
	count_list = [["PART","L1","L2","Total","Vruddhi","Not Vruddhi","Not sure"]]

	return main(29,"No",[],False,"y",2,count_list)

def run(n):
	count_list = [["PART","L1","L2","Total","Vruddhi","Not Vruddhi","Not sure"]]
	print main(n,"No",[],False,"y",2,count_list)

#print 'begin'
#run(1)