from collections import defaultdict
from collections import OrderedDict
import json
import io
import random

def combinations(index,node_dict,dic,count,vruddhi,ends_with,two_vowels,last_second,total):
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
	
	count_tot = 0
	report = 0
	count_0 = 0
	count_1 = 0
	removed = 0
	
	for key in dic:
		for each in dic[key]:
			result = [0,0,0,0]
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
			if check == 0:
				if len(each.split(" "))<2:
					continue
				if len(each.split(" "))==2:
					if int(each.split(" ")[1]) == 1:
						#print source,derived
						removed += 1
						continue


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
				if str(source)[len(source)-1] not in ends_with:
					result[1] = 1
				else:
					result[1] = 0
			else:
				result[1] = 0
			if len(each.split(" "))>1:
				if int(each.split(" ")[1]) is 0:
					count_0 += 1
				elif int(each.split(" ")[1]) is 1:
					count_1 += 1
				else:
					print "WTF"
				seeds_string += "N"+str(count+x)+'\t'+"L"+str(int(each.split(" ")[1])+1)+'\t'+"1.0\n"
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

	for i in range(len(yes)):
		for j in range(i+1,min(i+1001,len(yes))):
			weight = 0
			for k in range(4):
				if yes[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += yes[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"

	for i in range(len(no)):
		for j in range(i+1,min(i+501,len(no))):
			weight = 0
			for k in range(4):
				if no[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += no[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"

	for i in range(len(not_sure)):
		for j in range(i+1,min(i+501,len(not_sure))):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and not_sure[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += not_sure[i][0]+'\t'+not_sure[j][0]+'\t'+str(weight)+"\n"

	for i in range(len(not_sure)):
		for j in range(i+1,min(i+501,len(yes))):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			string += not_sure[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"

		for j in range(i+1,min(i+501,len(no))):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
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
	print removed,fish

	count_list = ["part"+str(index),count_0,count_1,count-1,num_vruddhi,not_vruddhi,not_sure_vruddhi]					
	return (node_dict,string,count,seeds_string,count_0,count_list)
					

def main(n,vruddhi,ends_with,two_vowels,last_second,total):
	count = 1
	node_dict = defaultdict(lambda : defaultdict(lambda : str))
	input_dict = defaultdict(lambda : defaultdict(lambda : list()))
	with open("part"+str(n)+"/"+"part"+str(n)+"_algo_file.txt") as f:
		input_dict = json.loads(f.read())
	f1 = open("part"+str(n)+"/"+"input_graph.txt",'wb')
	f2 = open("part"+str(n)+"/"+"seeds.txt",'wb')
	for key in input_dict:
		(node_dict,string,count,seeds_string,count_0,count_list) = combinations(n,node_dict,input_dict[key],count,vruddhi,ends_with,two_vowels,last_second,total)
	f1.write(string)
	f2.write(seeds_string)
	f1.close()
	f2.close()
	node_dict = OrderedDict(sorted(node_dict.items(), key=lambda t: t[0]))
	with io.open("part"+str(n)+"/"+"nodes_dict.txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(node_dict,indent=4,ensure_ascii=False,sort_keys=True)))
	print "part",n,count,"done"
	return count_list


def main_new():
	
	# main(1,True,[],False,"",1)
	# main(2,False,["a"],False,"",2)
	# main(3,True,[],False,"",1)
	# main(4,True,["f","F"],False,"",2)
	# main(5,"No",[],False,"",1)
	# main(6,"No",[],False,"",1)
	# main(7,True,["u","o"],False,"",2)
	# main(8,False,[],False,"",1)
	# main(9,"No",[],False,"",1)
	# main(10,"No",["f","F"],False,"",2)
	# main(11,False,["a"],False,"",2)
	# main(12,"No",[],False,"",1)
	# main(13,False,[],False,"",1)
	# main(14,"No",[],False,"",1)
	# main(16,"No",["i","I"],False,"",2)
	# main(17,False,["u"],False,"",1)
	# main(18,False,[],False,"",1)
	# main(19,"No",[],False,"",1)
	# main(20,"No",[],False,"",1)
	# main(21,"No",[],False,"",1)
	# main(22,"No",[],False,"",1)
	print main(23,True,["u","U","f"],True,"k",4)
	# main(24,"No",[],False,"",1)
	# main(25,False,[],False,"",1)
	# main(26,"No",["a"],False,"",2)
	# main(27,"No",[],False,"",1)
	# main(28,True,["u","U"],False,"",2)
	# main(29,"No",[],False,"y",2)
	# main(30,"No",[],False,"",1)


#main_new()
#commented line 110
