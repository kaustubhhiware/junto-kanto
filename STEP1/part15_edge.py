from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import time

def combinations(index,node_dict,dic,count,vruddhi,ends_with,two_vowels,
				starts_with,total,seed_analyze=0):
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
	test = ""
	count_0 = 0
	count_1 = 0
	for key in dic:
		for each in dic[key]:
			result = [0,0,0,0,0]
			temp = 0
			check = 100
			if len(each.split(" "))>2:
				fish += 1
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
			
			if len(source)<=2:
				continue
			try:
				if source[0] == starts_with:
					result[3] = 1
				else:
					result[3] = 0
			except IndexError:
				result[3] = 0
				
			while(temp<len(source)):
				if source[temp] in s_vow:
					if source[temp] == "a":
						if derived[temp] == "A":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "e" or source[temp] == "i"  or source[temp] == "I":
						if derived[temp] == "E":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "u" or source[temp] =="o"or source[temp] == "U":
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
			if type(vruddhi) is bool:
				if check is 1:
					if vruddhi:
						ans = 1
					else:
						ans = 0
				elif check is 0:
					if vruddhi:
						ans = 0
					else:
						ans = 1
				elif check is -1:
					ans = -1
				elif check is 100:
					errors+=1
					Error.append(x)
					check = -1
			else:
				ans = check			

			if len(ends_with)>0:
				if str(source)[len(source)-1] in ends_with:
					result[1] = 1
				else:
					result[1] = 0
			
				if source[len(source)-4:] in ends_with:
					result[4] = 1
				else:
					result[4] = 0

			if len(each.split(" "))>1:
				if int(each.split(" ")[1]) is 0:
					count_0 += 1
				else:
					count_1 += 1
				seeds_string += "N"+str(count+x)+'\t'+"L"+str(int(each.split(" ")[1])+1)+'\t'+"1.0\n"
			else:
				if vruddhi is True and check is 0:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1
				if vruddhi is False and check is 1:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1

			result[0] = 1
			temp_node_list = []
			temp_node_list.append("N"+str(count+x))
			temp_node_list.append(result)
			if ans is 1:
				yes.append(temp_node_list)
			elif ans is 0:
				no.append(temp_node_list)
			elif ans is -1:
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
	edgenVSG = 0

	for i in range(len(yes)):
		for j in range(i+1,len(yes)):
			weight = 0
			for k in range(5):
				if yes[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += yes[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"
			if yes[i][0] in setG and yes[j][0] in setS:
				edgeVSG += 1
			elif yes[i][0] in setS and yes[j][0] in setG:
				edgeVSG += 1

	for i in range(len(no)):
		for j in range(i+1,len(no)):
			weight = 0
			for k in range(5):
				if no[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += no[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"
			if no[i][0] in setG and no[j][0] in setS:
				edgenVSG += 1
			if no[i][0] in setS and no[j][0] in setG:
				edgenVSG += 1

	print "Vruddhi edges between Gold and Seeds : ",edgeVSG,"\n"
	print "non Vruddhi edges between Gold and Seeds : ",edgeVSG,"\n"
	time.sleep(1)

	for i in range(len(not_sure)):
		for j in range(i+1,len(not_sure)):
			weight = 0
			for k in range(5):
				if not_sure[i][1][k] == 1 and not_sure[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += not_sure[i][0]+'\t'+not_sure[j][0]+'\t'+str(weight)+"\n"

	for i in range(len(not_sure)):
		for j in range(len(yes)):
			weight = 0
			for k in range(5):
				if not_sure[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			string += not_sure[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"
		for j in range(len(no)):
			weight = 0
			for k in range(5):
				if not_sure[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			if weight<0:
				print "**** ERROR ****"

			string += not_sure[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"	
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
	if seed_analyze==1:
		return (node_dict,string,count,seeds_string,count_0,count_list,yes,no,not_sure)
	else:
		return (node_dict,string,count,seeds_string,count_0,count_list)
	
					

def main(n,vruddhi,ends_with,two_vowels,starts_with,total,seed_analyze=0):
	count = 1
	yes = []
	no = []
	not_sure = []

	node_dict = defaultdict(lambda : defaultdict(lambda : str))
	input_dict = defaultdict(lambda : defaultdict(lambda : list()))
	with open("part"+str(n)+"/"+"part"+str(n)+"_algo_file.txt") as f:
		input_dict = json.loads(f.read())
	f1 = open("part"+str(n)+"/"+"input_graph.txt",'wb')
	f2 = open("part"+str(n)+"/"+"seeds.txt",'wb')
	for key in input_dict:
		if seed_analyze==1:
			(node_dict,string,count,seeds_string,count_0,count_list,yes,no,not_sure) = combinations(n,node_dict,input_dict[key],count,vruddhi,ends_with,two_vowels,starts_with,total,seed_analyze)
		else:	
			(node_dict,string,count,seeds_string,count_0,count_list) = combinations(n,node_dict,input_dict[key],count,vruddhi,ends_with,two_vowels,starts_with,total,seed_analyze)
	f1.write(string)
	f2.write(seeds_string)
	f1.close()
	f2.close()
	node_dict = OrderedDict(sorted(node_dict.items(), key=lambda t: t[0]))
	with io.open("part"+str(n)+"/"+"nodes_dict.txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(node_dict,indent=4,ensure_ascii=False,sort_keys=True)))
	print "part",n,count-1,"done"
	if seed_analyze==1:
		return count_list,yes,no,not_sure
	else:
		return count_list


def main_new(seed_analyze=0):
	
	return main(15,"No",["i","pati"],True,"n",4,seed_analyze)

#main_new()
