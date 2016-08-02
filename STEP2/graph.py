import io
import json
from collections import defaultdict

def main(n):
	edge_weight = defaultdict(lambda:defaultdict(lambda:float))
	node_dict = defaultdict(lambda : defaultdict(lambda : str))
	with open("part"+str(n)+"/edge_weights.txt") as f:
		edge_weight = json.loads(f.read())
	with open("part"+str(n)+"/nodes_dict.txt") as f:
		dic1 = json.loads(f.read())
	f1 = open("part"+str(n)+"/input_graph.txt","wb")
	string = ""
	data = []
	count = 0


	for each in dic1:
		for key in dic1[each]:
			data.append([each,key,dic1[each][key][0].split(" ")[0]])
			temp_dic = {}
			temp_dic[key] = dic1[each][key][0] 
			node_dict[each] = temp_dic
			count+=1 
	dic = {}
	max_weight = 0.0
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			weight = 0.0
			if data[i][2] in edge_weight:
				if data[j][2] in edge_weight[data[i][2]]:
					weight = edge_weight[data[i][2]][data[j][2]]
			elif data[j][2] in edge_weight:
				if data[i][2] in edge_weight[data[j][2]]:
					weight = edge_weight[data[j][2]][data[i][2]]
			if weight == 0.0:
				continue
			dic["N"+str(data[i][0])+'\t'+"N"+str(data[j][0])+'\t'] = weight
			if weight > max_weight:
				max_weight = weight
	for key in dic:
		weight = dic[key]
		string  += key + str(weight/max_weight)+'\n'
	f1.write(string)
	with io.open("part"+str(n)+"/nodes_dict_step2.txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(node_dict,indent=4,ensure_ascii=False,sort_keys=True)))
	f1.close()
	f2 = open("part"+str(n)+"/label_prop_output_step1.txt",'r')
	f3 = open("part"+str(n)+"/seeds.txt",'wb')
	text = f2.read()
	data = text.split("\n")
	seeds_string = ""
	for each in data:
		if len(each.split("\t"))<2:
			#print "Error"# removed with Harsha's consent
			continue
		temp_s = each.split("\t")[0]
		temp_s += '\t'
		#print each#used for debugging
		if each.split("\t")[1] != "":
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
	
		seeds_string += temp_s

	f3.write(seeds_string)
	f3.close()
	print "part",n,count,"done"

#for i in range(1,31):
#	if i in [5,10,12,18,22,24]:
#		continue
#	main(i)
