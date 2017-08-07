import os
import random
from collections import defaultdict

def merge_graph(n):
	partdir = ""
	f2 = open(partdir+"Step2/input_graph.txt",'r')
	f3= open(partdir+"Step3/input_graph_unmerged.txt",'r')
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
	f = open(partdir+"Step3/input_graph.txt",'wb')
	f.write(string)
	f.close()

def runpyfile(filename):
	os.chmod(filename,0755)#mark executable first
	os.system("python2 "+filename)

def gen_gold(n,l1range,l2range,l1gold,l2gold):
	f = open("Step1/seeds.txt",'r')
	string = f.read()
	f.close()

	string = string.split("\n")
	seedout = ""
	excessout = ""
	goldout = ""
	for each in string:
		if(len(each.split("\t")) < 2):
			print "see"
			continue
		if each.split("\t")[1] == "L1":
			x = random.randrange(0,l1range)
			if x < l1gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"
		else:
			x = random.randrange(0,l2range)
			if x < l2gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"

	f = open("Step1/seeds.txt",'wb')
	f.write(seedout)
	f.close()

	f = open("gold_labels.txt",'wb')
	f.write(excessout)
	f.close()

def main(n):
	os.chdir("part"+str(n)+"/")
	runpyfile("1_graph.py")
	print "----->",n," finished 1_graph"
	# generating gold for each file
	if n==23:
		gen_gold(n,100,100,50,30)
	else:
		gen_gold(n,100,100,50,50)
	os.system("junto config junto1")
	print "----->",n," finished junto1"

	runpyfile("2_graph.py")
	print "----->",n," finished 2_graph"

	os.system("junto config junto2")
	print "----->",n," finished junto2"

	runpyfile("3_graph.py")
	merge_graph(n)
	print "----->",n," finished 3_graph"

	os.system("junto config junto3")
	print "----->",n," finished junto3"

	os.chdir("..")

main(2)
