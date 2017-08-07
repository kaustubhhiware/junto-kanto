from collections import defaultdict

def main(n):
	f2 = open("Step2/input_graph.txt",'r')
	f3= open("Step3/input_graph_unmerged.txt",'r')
	text2 = f2.read()
	text3 = f2.read()
	data2 = text2.split('\n')
	data3 = text3.split('\n')
	dic = defaultdict(lambda:defaultdict(lambda:float))
	for each in data2:
		try:
			temp = each.split('\t')
			dic[temp[0]][temp[1]] = float(temp[2])
		except IndexError:
			print "IndexError1"
	for each in data3:
		try:
			temp = each.split('\t')
			if temp[0] in dic:
				if temp[1] in dic[temp[0]]:
					dic[temp[0]][temp[1]] += float(temp[2])
				else:
					dic[temp[0]][temp[1]] = float(temp[2])
			else:
				dic[temp[0]][temp[1]] = float(temp[2])
		except IndexError:
			print "IndexError"
	string = ""
	for key in dic:
		for each in dic[key]:
			string += key + '\t' + each +'\t'+ str(dic[key][each])+'\n'
	f = open("Step3/input_graph.txt",'wb')
	f.write(string)
	f.close()
"""
for i in range(11,12):
	if i in [5,10,12,18,22,24]:
		continue
	main(i)
"""
main(2)