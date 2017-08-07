import io
import json
from collections import defaultdict
from scipy import spatial
import numpy as np

temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
indices = {}
for i in range(len(temp)):
	indices[temp[i]] = i
vector_data = []
no_data = ["F","H","M","L","W","V","X","Z","x"]
for key in indices:
	with open("../data/"+key+".txt",'r') as f:
		dic1 = defaultdict(lambda:defaultdict(lambda:list))
		print key,
		if key not in no_data:
			dic1 = json.loads(f.read())
		vector_data.append(dic1)
print
def main(n):
	f = open("Step1/input_graph.txt",'r')
	text = f.read()
	data = text.split("\n")
	nodes = {}
	for each in data:
		try:
			if each.split('\t')[0] in nodes:
				nodes[each.split('\t')[0]].append(each.split('\t')[1])
			else:
				nodes[each.split('\t')[0]] = [each.split('\t')[1]]
		except IndexError:

			print "IndexError",each
	with open("nodes_dict.txt") as f:
		dic1 = json.loads(f.read())
	source = {}
	for key in dic1:
		for each in dic1[key]:
			temp = dic1[key][each][0]
		if len(temp.split(" "))>2:
			print "Error"
			continue
		elif len(temp.split(" "))==2:
			source['N'+key]= temp.split(" ")[0]
		else:
			source['N'+key]= temp

	result_vector = {}
	string = ""
	for key in nodes:
		for each in nodes[key]:
			check = 1
			s1 = source[key]
			s2 = source[each]
			maximum = 0.0

			if s1 in vector_data[indices[s1[0]]]:
				result_vector[s1] = len(vector_data[indices[s1[0]]][s1])
			else:
				result_vector[s1] = 0

			if s2 in vector_data[indices[s2[0]]]:
				result_vector[s2] = len(vector_data[indices[s2[0]]][s2])
			else:
				result_vector[s2] = 0			

			if s1 in vector_data[indices[s1[0]]] and s2 in vector_data[indices[s2[0]]]:
				for every1 in vector_data[indices[s1[0]]][s1]:
					for every2 in vector_data[indices[s2[0]]][s2]:
						dataSetI = np.array(vector_data[indices[s1[0]]][s1][every1],dtype = float)
						dataSetII = np.array(vector_data[indices[s2[0]]][s2][every2],dtype = float)
						result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
						if result>maximum:
							maximum = result
				string += key + '\t' + each + '\t' + str(maximum) +'\n'

	f = open("Step3/input_graph_unmerged.txt",'wb')
	f.write(string)
	f.close()
	f2 = open("Step2/label_prop_output.txt",'r')
	f3 = open("Step3/seeds.txt",'wb')
	text = f2.read()
	data = text.split("\n")
	seeds_string = ""
	err_count = 0
	for each in data:
		if len(each.split("\t"))<2:
			#print "Error"
			continue
		temp_s = each.split("\t")[0]
		temp_s += '\t'
		try:
			if each.split("\t")[1].split(" ")[1] == "1.0" or each.split("\t")[2].split(" ")[1] == "1.0":
				temp_s += each.split("\t")[1].split(" ")[0]+'\t'
				temp_s += each.split("\t")[1].split(" ")[1]+'\n'
			else:
				for i in range(5):
					if each.split("\t")[3].split(" ")[i] == "__DUMMY__":
						break
				j = 0
				check = 0
				while(j<5):
					if j==i:
						j+=2
						continue
					if check == 0:
						temp_s += each.split("\t")[3].split(" ")[j]+'\t'+each.split("\t")[3].split(" ")[j+1]+'\n'
						temp_s += each.split("\t")[0]
						temp_s += '\t'
						check = 1
					else:
						temp_s += each.split("\t")[3].split(" ")[j]+'\t'+each.split("\t")[3].split(" ")[j+1]+'\n'
					j+=2
		except IndexError:
			err_count +=1 
			continue
	
		seeds_string += temp_s
	print err_count,"errors"
	print n,"done"
	f3.write(seeds_string)
	f3.close()

	with io.open("vector_dict.txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(result_vector,indent=4,ensure_ascii=False,sort_keys=True)))
"""
for i in range(11,12):
	if i in [5,10,12,18,22,24]:
		continue
	main(i)
"""
main(2)